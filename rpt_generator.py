
"""
Copyright@ Jian Wu,wujian1112@126.com,2022. If use or build on the code, please cite it at
URL https://github.com/wujian1112/DLMDP
"""
"""
To generate random_powerlaw_tree saved in 'data/random_powerlaw_tree/'
"""

from models_for_data import random_graph_data as rgd
import numpy as np
import pickle
import os
import random

# save data
savepath= 'data/random_powerlaw_tree/'
a= os.path.exists(savepath)
if not a:
    os.makedirs(savepath)

# data parameters
nodes_list =  list(range(10,101))
random.shuffle(nodes_list)
tries = 50000

# generate data
information = dict()
graph_list = []
node_total = 0
edge_total = 0
num_graph = 1000

for i in range(num_graph):
    graph = dict()
    g_obj = rgd.random_graph()
    print('graph_i = ',  i)

    num_node = np.random.choice(nodes_list, replace=True)
    adjacency_matrix,labels_vector,G = g_obj.random_powerlaw_tree(num_node, tries, gamma=3,seed=None)
    num_edge = G.number_of_edges()

    node_total += num_node
    edge_total += num_edge

    graph["num_node"] = num_node
    graph["num_edge"] = num_edge
    graph["adj"] = adjacency_matrix
    graph["labels"] = labels_vector
    graph_list.append(graph)

information["num_graph"] = num_graph
information["node_ave"] = node_total/num_graph
information["edge_ave"] = edge_total/num_graph
graph_list.append(information)

path = savepath + "rpt.pkl"

with open(path, "wb") as f:
    pickle.dump(graph_list, f)








