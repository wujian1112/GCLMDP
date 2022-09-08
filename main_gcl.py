

import function_tool as ft
from torch_geometric.loader import DataLoader
from torch_geometric.utils import from_networkx,unbatch
from torch_scatter import scatter_mean
import torch_geometric as tg



import torch
savepath= 'data/ring_of_cliques/'
path = savepath + "rc.pkl"

dataset = ft.load_pyg_data(path)
loader = DataLoader(dataset, batch_size=2, shuffle=True)

for data in loader:
    # print(data.num_graphs)
    print(data.num_edges)
    #x = scatter_mean(data.x, data.batch, dim=0)
    #print(x,x.size())












