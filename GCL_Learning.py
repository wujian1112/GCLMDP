

import os
import torch
import GCL.losses as L
import GCL.augmentors as A
import torch.nn.functional as F

from torch import nn
from tqdm import tqdm
from torch.optim import Adam
from GCL.eval import get_split, SVMEvaluator
from GCL.models import DualBranchContrast
from torch_geometric.nn import GINConv, global_add_pool
from torch_geometric.loader import DataLoader
from torch_geometric.datasets import TUDataset
import function_tool as ft
import random

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def make_gin_conv(input_dim, out_dim):

    return GINConv(nn.Sequential(nn.Linear(input_dim, out_dim), nn.ReLU(), nn.Linear(out_dim, out_dim)))


class GConv(nn.Module):
    def __init__(self, input_dim, hidden_dim, num_layers):
        super(GConv, self).__init__()
        self.layers = nn.ModuleList()
        self.batch_norms = nn.ModuleList()

        for i in range(num_layers):
            if i == 0:
                self.layers.append(make_gin_conv(input_dim, hidden_dim))
            else:
                self.layers.append(make_gin_conv(hidden_dim, hidden_dim))
            self.batch_norms.append(nn.BatchNorm1d(hidden_dim))

        project_dim = hidden_dim * num_layers
        self.project = torch.nn.Sequential(
            nn.Linear(project_dim, project_dim),
            nn.ReLU(inplace=True),
            nn.Linear(project_dim, project_dim))

    def forward(self, x, edge_index, batch):
        z = x
        zs = []
        for conv, bn in zip(self.layers, self.batch_norms):
            z = conv(z, edge_index)
            z = F.leaky_relu(z)
            z = bn(z)
            zs.append(z)
        # print(zs[0].shape)
        gs = [global_add_pool(z, batch) for z in zs]
        #print(gs[0].shape)


        z, g = [torch.cat(x, dim=1) for x in [zs, gs]]
        # print(z.shape)

        return z, g


class Encoder(torch.nn.Module):
    def __init__(self, encoder, augmentor):
        super(Encoder, self).__init__()
        self.encoder = encoder
        self.augmentor = augmentor

    def forward(self, x, edge_index, batch):
        aug1, aug2 = self.augmentor
        x1, edge_index1, edge_weight1 = aug1(x, edge_index)
        x2, edge_index2, edge_weight2 = aug2(x, edge_index)
        z, g = self.encoder(x, edge_index, batch)
        z1, g1 = self.encoder(x1, edge_index1, batch)
        z2, g2 = self.encoder(x2, edge_index2, batch)
        return z, g, z1, z2, g1, g2


def train(encoder_model, contrast_model, dataloader, optimizer):
    encoder_model.train()
    epoch_loss = 0
    for data in dataloader:
        data = data.to(device)
        # to verify node num and label num
        # print('nodes=',data.x.shape)
        # print('label=',data.y.shape)
        optimizer.zero_grad()

        if data.x is None:
            num_nodes = data.batch.size(0)
            data.x = torch.ones((num_nodes, 1), dtype=torch.float32, device=data.batch.device)

        _, _, _, _, g1, g2 = encoder_model(data.x, data.edge_index, data.batch)
        # save model
        save_model_path = 'model_weights/'
        model_file = 'rc_bg_model.pkl'
        model_path = save_model_path + model_file
        a = os.path.exists(save_model_path)
        if not a:
            os.makedirs(save_model_path)
        torch.save(encoder_model.state_dict(), model_path)

        g1, g2 = [encoder_model.encoder.project(g) for g in [g1, g2]]
        loss = contrast_model(g1=g1, g2=g2, batch=data.batch)
        loss.backward()
        optimizer.step()

        epoch_loss += loss.item()
    return epoch_loss


def test(encoder_model, dataloader):
    encoder_model.eval()
    x = []
    y = []
    for data in dataloader:
        data = data.to(device)
        if data.x is None:
            num_nodes = data.batch.size(0)  # get the number of size
            data.x = torch.ones((num_nodes, 1), dtype=torch.float32, device=data.batch.device)
        _, g, _, _, _, _ = encoder_model(data.x, data.edge_index, data.batch)
        x.append(g)
        y.append(data.y)
    x = torch.cat(x, dim=0)
    y = torch.cat(y, dim=0)
    print(x.shape)
    print(y.shape)

    split = get_split(num_samples=x.size()[0], train_ratio=0.8, test_ratio=0.1)
    result = SVMEvaluator(linear=True, params={
                                               'dual': [False],

                                              })(x, y, split)


    return result


def main():

    # dataset= TUDataset(root='dataset_benchmark/PTC_MR', name='PTC_MR', use_node_attr=True)

    # /////////////////////////////////////////////

    # p = 0.9
    # savepath = 'data/gnp_random_graph/'
    # path = savepath + "gnp_{}.pkl".format(p)

    # savepath= 'data/random_powerlaw_tree/'
    # path = savepath + "rpt.pkl"

    # savepath = 'data/random_tree/'
    # path = savepath + "rt.pkl"

    # savepath = 'data/ring_of_cliques/'
    # path = savepath + "rc.pkl"

    # savepath = 'data/barbell_graph/'
    # path = savepath + "bg.pkl"

    # ///////////////////////////////////////////
    # p = 0.9
    # savepath = 'data/crg_gnp_random_graph/'
    # path = savepath + "crg_gnp_{}.pkl".format(p)
    # label_list = ['crg','gnp']

    # savepath = 'data/rpt_rt_tree_graph/'
    # path = savepath + "rpt_rt.pkl"
    # label_list = ['rpt', 'rt']

    savepath = 'data/rc_bg_graph/'
    path = savepath + "rc_bg.pkl"
    label_list = ['rc', 'bg']

    dataset = ft.load_pyg_data_2(path,label_list)
    random.shuffle(dataset)

    dataloader = DataLoader(dataset, batch_size=32, shuffle=True)


    input_dim = 1
    # dataloader = DataLoader(dataset, batch_size=128)
    # input_dim = max(dataset.num_features, 1)


    # aug1 = A.Identity()
    # aug2 = A.RWSampling(num_seeds=100, walk_length=10)


    aug1 = A.RandomChoice([A.RWSampling(num_seeds=1000, walk_length=10),
                           A.NodeDropping(pn=0.1),
                           A.FeatureMasking(pf=0.1),
                           A.EdgeRemoving(pe=0.1),
                           ],1)
    aug2 = A.RandomChoice([A.RWSampling(num_seeds=1000, walk_length=10),
                      A.NodeDropping(pn=0.1),
                      A.FeatureMasking(pf=0.1),
                      A.EdgeRemoving(pe=0.1)],1)

    gconv = GConv(input_dim=input_dim, hidden_dim=32, num_layers=2).to(device)
    encoder_model = Encoder(encoder=gconv, augmentor=(aug1, aug2)).to(device)
    contrast_model = DualBranchContrast(loss=L.InfoNCE(tau=0.2), mode='G2G').to(device)


    optimizer = Adam(encoder_model.parameters(), lr=0.01)

    with tqdm(total=100, desc='(T)') as pbar:
        for epoch in range(1, 101):
            loss = train(encoder_model, contrast_model, dataloader, optimizer)
            pbar.set_postfix({'loss': loss})
            pbar.update()

    test_result = test(encoder_model, dataloader)
    print(f'(E): Best test F1Mi={test_result["micro_f1"]:.4f}, '
          f'F1Ma={test_result["macro_f1"]:.4f}，'
          f'test_acc={test_result["test_acc"]:.4f}')



    # # load model data
    # new_encoder_model = Encoder(encoder=gconv, augmentor=(aug1, aug2))
    # new_encoder_model.load_state_dict(torch.load(save_model_path)).to(device)
    #
    # test_result = test(encoder_model, dataloader)
    # print(f'(E): Best test F1Mi={test_result["micro_f1"]:.4f}, '
    #       f'F1Ma={test_result["macro_f1"]:.4f}，'
    #       f'test_acc={test_result["test_acc"]:.4f}')



if __name__ == '__main__':
    main()