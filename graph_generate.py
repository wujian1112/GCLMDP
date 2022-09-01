
"""
Copyright@ Jian Wu,wujian1112@126.com,2022. If use or build on the code, please cite it at
URL https://github.com/wujian1112/DLMDP
"""

from models_for_data import pre_process_data as ppd
from models_for_data import random_graph_data as rgd
from visualization import graph_visualization as gv
from operation import matrix
import networkx as nx
import numpy as np
import pickle
import os

savepath= 'data/clustered_random_graph/'
a= os.path.exists(savepath)
if not a:
    os.makedirs(savepath)

# object for graphs
g_obj = rgd.random_graph()
plot_obj = gv.visal_graph()
graph =dict()

num_nodes,num_clusters,pin,pout = 20,4,0.2,0.01  # 0.001
nodes_list = list(range(20,101))
cluster_list = list(range(2,6))
pin_list = [0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
pout = 0.01
a,v,G = g_obj.clustered_random_graph(num_nodes,num_clusters,pin,pout)

graph["num_node"] = G.numberOfNodes()
graph["num_edge"] = G.numberOfEdges()
graph["adj"] = a
graph["labels"] = v
print(graph)


plot_obj.graph_from_numpy_plot(a)

data = ["label1", "label2", "label3", "label4", "label_i"]
path = savepath + "shiyan.pkl"
for d in data:
    with open(path, "ab+") as f:
        pickle.dump(d, f)






