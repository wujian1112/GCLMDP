import pickle
from torch_geometric.loader import DataLoader
from torch_geometric.utils import from_networkx
import networkx as nx
import torch



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