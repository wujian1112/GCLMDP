
import torch
import GCL.augmentors as A
import torch.nn.functional as F

from torch import nn
from torch_geometric.nn import GINConv, global_add_pool
from torch_geometric.loader import DataLoader
import function_tool as ft
import os





# load GNN encoder
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
input_dim = 1

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

modelsavepath = 'model_weights/'
modelfilename = 'rc_bg_model.pkl'
model_path = modelsavepath + modelfilename
encoder_model.load_state_dict(torch.load(model_path))

# load star graph data
# it is selected according to the dataset
datasetname = 'crg_gnp_random_graph' # 'crg_gnp_random_graph', 'rpt_rt_tree_graph','rc_bg_graph'
graphname = 'crg_gnp_0.5' # 'crg_gnp_p' p=0.2-0.9. 'rpt_rt','rc_bg'
label_list = ['crg', 'gnp'] # ['crg', 'gnp'], ['rpt', 'rt'], ['rc', 'bg']
# location
datasavepath = 'data/{}/'.format(datasetname)
datafilename = '{}_star.pkl'.format(graphname)
ispath = datasavepath + datafilename
# loading
a = os.path.exists(ispath)
if a:
    dataset = ft.load_data(ispath)
else:
    o_savepath = datasavepath
    o_path = o_savepath + "{}.pkl".format(graphname)
    label_list = label_list
    dataset= ft.load_pyg_data_2(o_path,label_list)
    dataset = ft.load_star_data(dataset, o_savepath, datafilename, encoder_model, device)


print(dataset[0])

# learning to sampling

