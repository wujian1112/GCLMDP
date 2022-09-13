
"""
Copyright@ Jian Wu,wujian1112@126.com,2022. If use or build on the code, please cite it at
URL https://github.com/wujian1112/DLMDP
"""
"""
To generate gnp_random_graph saved in 'data/rpt_rt_graph/'
"""

from DLMDP.function_datasets import random_graph_data as rgd
from DLMDP.visualization import graph_visualization as gv
import numpy as np
import pickle
import os
import random

# save data
savepath= 'data/rpt_rt_tree_graph/'
a= os.path.exists(savepath)
if not a:
    os.makedirs(savepath)

g_obj = rgd.random_graph()
# data parameters
rpt_nodes_list =  list(range(10,101))
random.shuffle(rpt_nodes_list)
rt_nodes_list =  list(range(10,101))
random.shuffle(rt_nodes_list)
tries = 50000

crg_nodes_list =  list(range(20,101))
random.shuffle(crg_nodes_list)

gnp_nodes_list =  list(range(10,101))
random.shuffle(gnp_nodes_list)

rpt_graph_label = 'rpt'
rt_graph_label = 'rt'


information = dict()
graph_list = []
node_total = 0
edge_total = 0
num_graph_1 = 1000
num_graph_2 = 1000

# generate rpt tree graph
for i in range(num_graph_1):
    graph = dict()
    g_obj = rgd.random_graph()
    print('graph_i = ', i)

    num_node = np.random.choice(rpt_nodes_list, replace=True)
    adjacency_matrix, labels_vector, G = g_obj.random_powerlaw_tree(num_node, tries, gamma=3, seed=None)
    num_edge = G.number_of_edges()

    node_total += num_node
    edge_total += num_edge

    graph["num_node"] = num_node
    graph["num_edge"] = num_edge
    graph["adj"] = adjacency_matrix
    graph["labels"] = labels_vector
    graph_list.append(graph)
    graph["label"] = rpt_graph_label
    graph_list.append(graph)

# generate rt tree graph
for j in range(num_graph_2):
    graph = dict()
    g_obj = rgd.random_graph()
    print('graph_j = ', j)

    n = np.random.choice(rt_nodes_list, replace=True)

    adjacency_matrix, labels_vector, G = g_obj.random_tree(n, seed=None, create_using=None)
    num_edge = G.number_of_edges()
    num_node = G.number_of_nodes()

    node_total += num_node
    edge_total += num_edge

    graph["num_node"] = num_node
    graph["num_edge"] = num_edge
    graph["adj"] = adjacency_matrix
    graph["labels"] = labels_vector
    graph["label"] = rt_graph_label
    graph_list.append(graph)

information["num_graph"] = num_graph_1 + num_graph_2
information["node_ave"] = node_total/(num_graph_1 + num_graph_2)
information["edge_ave"] = edge_total/(num_graph_1 + num_graph_2)
graph_list.append(information)

# save the graphs
path = savepath + "rpt_rt.pkl"
with open(path, "wb") as f:
    pickle.dump(graph_list, f)