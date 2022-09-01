
"""
Copyright@ Jian Wu,wujian1112@126.com,2022. If use or build on the code, please cite it at
URL https://github.com/wujian1112/DLMDP
"""
"""
To generate random_tree saved in 'data/random_tree/'
"""

from models_for_data import random_graph_data as rgd
from visualization import graph_visualization as gv
import numpy as np
import pickle
import os
import random

# save data
savepath= 'data/random_tree/'
a= os.path.exists(savepath)
if not a:
    os.makedirs(savepath)

# view graph
#plot_obj = gv.visal_graph()

# data parameters
nodes_list =  list(range(10,101))
# m1_list = list(range(3,11))
random.shuffle(nodes_list)
# m2_list = list(range(1,101))
# random.shuffle(m2_list)
#tries = 1e+10
#p_list = [0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]

# view graph
# adjacency_matrix,labels_vector,G = g_obj.gnp_random_graph(n, p, seed=None)
# print(labels_vector)
# plot_obj.graph_from_nx_plot(G)

# generate data


information = dict()
graph_list = []
node_total = 0
edge_total = 0
node_ave = 0
edge_ave = 0
num_graph = 1000

for i in range(num_graph):
    graph = dict()
    g_obj = rgd.random_graph()
    print('graph_i = ',  i)

    n = np.random.choice(nodes_list, replace=True)

    adjacency_matrix,labels_vector,G = g_obj.random_tree(n, seed=None, create_using=None)
    num_edge = G.number_of_edges()
    num_node = G.number_of_nodes()

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

path = savepath + "rt.pkl"

with open(path, "wb") as f:
    pickle.dump(graph_list, f)








