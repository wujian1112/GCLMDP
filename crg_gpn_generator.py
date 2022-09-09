
"""
Copyright@ Jian Wu,wujian1112@126.com,2022. If use or build on the code, please cite it at
URL https://github.com/wujian1112/DLMDP
"""
"""
To generate gnp_random_graph saved in 'data/gnp_random_graph/'
"""

from DLMDP.function_datasets import random_graph_data as rgd
from DLMDP.visualization import graph_visualization as gv
import numpy as np
import pickle
import os
import random

# save data
savepath= 'data/crg_gnp_random_graph/'
a= os.path.exists(savepath)
if not a:
    os.makedirs(savepath)

g_obj = rgd.random_graph()


crg_nodes_list =  list(range(20,101))
random.shuffle(crg_nodes_list)

gnp_nodes_list =  list(range(10,101))
random.shuffle(gnp_nodes_list)

crg_cluster_list = list(range(2,6))
random.shuffle(crg_cluster_list)
# pin_list = [0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
pin_list = [0.9]
crg_graph_label = 'crg'
gnp_graph_label = 'gnp'

for pin in pin_list:
    information = dict()
    graph_list = []
    node_total = 0
    edge_total = 0
    node_ave = 0
    edge_ave = 0
    num_graph_1 = 1000
    num_graph_2 = 1000

    # generate crg graph
    for i in range(num_graph_1):
        pout = 0.01
        graph = dict()
        g_obj = rgd.random_graph()
        print('pin,graph_i = ', pin, i)
        num_node = np.random.choice(crg_nodes_list, replace=True)
        num_cluster = np.random.choice(crg_cluster_list, replace=True)
        adjacency_matrix,labels_vector,G = g_obj.clustered_random_graph(num_node,num_cluster,pin,pout)
        num_edge = G.numberOfEdges()

        node_total += num_node
        edge_total += num_edge

        graph["num_node"] = num_node
        graph["num_edge"] = num_edge
        graph["adj"] = adjacency_matrix
        graph["labels"] = labels_vector
        graph["label"] = crg_graph_label
        graph_list.append(graph)

    # generate gnp graph
    for i in range(num_graph_2):
        graph = dict()
        g_obj = rgd.random_graph()
        print('p,graph_i = ', pin, i)
        num_node = np.random.choice(gnp_nodes_list, replace=True)

        adjacency_matrix,labels_vector,G = g_obj.gnp_random_graph(num_node, pin, seed=None)
        num_edge = G.number_of_edges()

        node_total += num_node
        edge_total += num_edge

        graph["num_node"] = num_node
        graph["num_edge"] = num_edge
        graph["adj"] = adjacency_matrix
        graph["labels"] = labels_vector
        graph["label"] = gnp_graph_label
        graph_list.append(graph)

    information["num_graph"] = num_graph_1 + num_graph_2
    information["node_ave"] = node_total/(num_graph_1 + num_graph_2)
    information["edge_ave"] = edge_total/(num_graph_1 + num_graph_2)
    graph_list.append(information)

    # save the graphs
    path = savepath + "crg_gnp_{}.pkl".format(pin)
    with open(path, "wb") as f:
        pickle.dump(graph_list, f)