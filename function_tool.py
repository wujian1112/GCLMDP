import pickle as pkl
from torch_geometric.loader import DataLoader
from torch_geometric.utils import from_networkx
import networkx as nx
import torch
from tqdm import tqdm





def load_data(path):
    my_data = pkl.load(open(path, 'rb'))

    return my_data

def load_pyg_data(path):
    datasets = []
    dataset = load_data(path)

    for i in range(len(dataset)-1):
        g = nx.from_scipy_sparse_matrix(dataset[i]['adj'])
        data = from_networkx(g)
        data.x = torch.ones((dataset[i]['num_node'], 1), dtype=torch.float32)
        data.y = torch.tensor(dataset[i]['labels'])#.reshape(-1,1)
        data.weight = None
        datasets.append(data)
    return datasets


def load_pyg_data_2(path,label_list):
    datasets = []
    dataset = load_data(path)


    num_graph = len(dataset)-1
    with tqdm(total=num_graph, desc='(L)') as pbar:
        for i in range(num_graph):
            g = nx.from_scipy_sparse_matrix(dataset[i]['adj'])
            data = from_networkx(g)
            data.x = torch.ones((dataset[i]['num_node'], 1), dtype=torch.float32)
            for j in range(len(label_list)):
                if dataset[i]['label'] == label_list[j]:
                    data.y = torch.tensor([j],dtype=torch.int32)
            data.weight = None
            datasets.append(data)
            pbar.set_postfix({'loading | graph id': i})
            pbar.update()

    return datasets


# def to_star_data(encoder_model, dataset,device):
#     encoder_model.eval()
#     dataloader = DataLoader(dataset, batch_size=1, shuffle=False)
#     data = None
#
#     return data

def satr_graph(node_num):
    g = nx.star_graph(node_num, create_using=None)
    g = from_networkx(g)

    return g


def load_star_data(dataset,o_savepath ,datafilename,encoder_model,device):
    datasets = []
    encoder_model.eval()
    dataloader = DataLoader(dataset, batch_size=1, shuffle=False)
    num_graph = len(dataset)

    with tqdm(total=num_graph, desc='(C)') as pbar:
        for data in dataloader:
            star_g = satr_graph(data.x.shape[0])
            data = data.to(device)
            z, g, _, _, _, _ = encoder_model(data.x, data.edge_index, data.batch)
            star_g.x = torch.cat([g.detach(), z.detach()], dim=0)

            datasets.append(star_g)
            pbar.update()
        # save the graphs
    star_path = o_savepath + datafilename
    with open(star_path, "wb") as f:
        pkl.dump(datasets, f)
    return datasets



