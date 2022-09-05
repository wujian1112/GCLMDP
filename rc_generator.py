
"""
Copyright@ Jian Wu,wujian1112@126.com,2022. If use or build on the code, please cite it at
URL https://github.com/wujian1112/DLMDP
"""
"""
To generate ring_of_cliques saved in 'data/ring_of_cliques/'
"""

from models_for_data import random_graph_data as rgd
import numpy as np
import pickle
import os
import random

# save data
savepath= 'data/ring_of_cliques/'
a= os.path.exists(savepath)
if not a:
    os.makedirs(savepath)


# data parameters

cliquesize_list = list(range(3,11))
random.shuffle(cliquesize_list)
num_cliques_list = list(range(3,11))
random.shuffle(num_cliques_list)

# generate data

information = dict()
graph_list = []
node_total = 0
edge_total = 0
num_graph = 500

for i in range(num_graph):
    print('graph_i = ', i)

    graph = dict()
    g_obj = rgd.random_graph()

    num_cliques = np.random.choice(num_cliques_list, replace=True)
    clique_size = np.random.choice(cliquesize_list, replace=True)

    adjacency_matrix,labels_vector,G = g_obj.ring_cliques(num_cliques, clique_size)

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

path = savepath + "rc.pkl"

with open(path, "wb") as f:
    pickle.dump(graph_list, f)








