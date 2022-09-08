from torch_geometric.datasets import TUDataset
from torch_geometric.datasets import Planetoid
from torch_geometric.loader import DataLoader
import torch_geometric.utils as tu


# 'ENZYMES'
dataset_benchmark  = TUDataset(root='dataset_benchmark/ENZYMES', name='ENZYMES', use_node_attr=True)

loader = DataLoader(dataset_benchmark, batch_size=3, shuffle=True)

for data in loader:
    #print(tu.unbatch(data.x,batch=data.batch,dim=0))
    print(data.batch.size(0))  # get the number of size

# 'Cora'
# dataset_benchmark  = Planetoid(root='dataset_benchmark/Cora', name='Cora')
# print(dataset_benchmark[0].has_isolated_nodes())



# for i in range(len(dataset_benchmark)):
#     print(dataset_benchmark[i].has_isolated_nodes())