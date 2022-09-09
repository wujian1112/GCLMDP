import pickle
from torch_geometric.loader import DataLoader
from torch_geometric.utils import from_networkx
import networkx as nx
import torch
from tqdm import tqdm




def load_data(path):
    my_data = pickle.load(open(path, 'rb'))

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


def to_star_graph(g_feature, node_feature,node_num):
    g = nx.star_graph(node_num, create_using=None)
    data = from_networkx(g)
    feature = torch.cat([g_feature,node_feature],dim=0)
    data.x = feature
    data.y = None
    data.weight = None
    return data


def to_star_data(structure_encoder, pyg_data):
    z, g, _, _, _, _ = structure_encoder(pyg_data.x, pyg_data.edge_index, 1)
    data = to_star_graph(g[0], z[0], z[0].shape[0])
    return data



