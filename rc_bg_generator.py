
"""
Copyright@ Jian Wu,wujian1112@126.com,2022. If use or build on the code, please cite it at
URL https://github.com/wujian1112/DLMDP
"""
"""
To generate gnp_random_graph saved in 'data/rc_bg_graph/'
"""

from DLMDP.function_datasets import random_graph_data as rgd
# from DLMDP.visualization import graph_visualization as gv
import numpy as np
import pickle
import os
import random

# save data
savepath= 'data/rc_bg_graph/'
a= os.path.exists(savepath)
if not a:
    os.makedirs(savepath)

g_obj = rgd.random_graph()
# data parameters
cliquesize_list = list(range(3,15))
random.shuffle(cliquesize_list)
num_cliques_list = list(range(3,15))
random.shuffle(num_cliques_list)

m1_list = list(range(3,50))
random.shuffle(m1_list)
m2_list = list(range(1,20))
random.shuffle(m2_list)

rc_graph_label = 'rc'
bg_graph_label = 'bg'


information = dict()
graph_list = []
node_total = 0
edge_total = 0
num_graph_1 = 1000
num_graph_2 = 1000

# generate rpt tree graph
for i in range(num_graph_1):
    print('graph_i = ', i)

    graph = dict()
    g_obj = rgd.random_graph()

    num_cliques = np.random.choice(num_cliques_list, replace=True)
    clique_size = np.random.choice(cliquesize_list, replace=True)

    adjacency_matrix, labels_vector, G = g_obj.ring_cliques(num_cliques, clique_size)

    num_edge = G.number_of_edges()
    num_node = G.number_of_nodes()

    node_total += num_node
    edge_total += num_edge

    graph["num_node"] = num_node
    graph["num_edge"] = num_edge
    graph["adj"] = adjacency_matrix
    graph["labels"] = labels_vector
    graph["label"] = rc_graph_label
    graph_list.append(graph)

# generate rt tree graph
for j in range(num_graph_2):
    graph = dict()
    g_obj = rgd.random_graph()
    print('graph_j = ', j)

    m1 = np.random.choice(m1_list, replace=True)
    m2 = np.random.choice(m2_list, replace=True)
    adjacency_matrix, labels_vector, G = g_obj.barbell_graph(m1, m2, create_using=None)
    num_edge = G.number_of_edges()
    num_node = G.number_of_nodes()

    node_total += num_node
    edge_total += num_edge

    graph["num_node"] = num_node
    graph["num_edge"] = num_edge
    graph["adj"] = adjacency_matrix
    graph["labels"] = labels_vector
    graph["label"] = bg_graph_label
    graph_list.append(graph)

information["num_graph"] = num_graph_1 + num_graph_2
information["node_ave"] = node_total/(num_graph_1 + num_graph_2)
information["edge_ave"] = edge_total/(num_graph_1 + num_graph_2)
graph_list.append(information)

# save the graphs
path = savepath + "rc_bg.pkl"
with open(path, "wb") as f:
    pickle.dump(graph_list, f)