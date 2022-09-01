
"""
Copyright@ Jian Wu,wujian1112@126.com,2022. If use or build on the code, please cite it at
URL https://github.com/wujian1112/DLMDP
"""
"""
To generate clustered_random_graph saved in 'data/clustered_random_graph/'
"""
from models_for_data import random_graph_data as rgd
import numpy as np
import pickle
import os
import random

savepath= 'data/clustered_random_graph/'
a= os.path.exists(savepath)
if not a:
    os.makedirs(savepath)

nodes_list =  list(range(20,101))
random.shuffle(nodes_list)
cluster_list = list(range(2,6))
random.shuffle(cluster_list)
pin_list = [0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]

for pin in pin_list:
    information = dict()
    graph_list = []
    node_total = 0
    edge_total = 0
    node_ave = 0
    edge_ave = 0
    num_graph = 5000
    pout = 0.01
    for i in range(num_graph):
        graph = dict()
        g_obj = rgd.random_graph()
        print('pin,graph_i = ', pin, i)
        num_node = np.random.choice(nodes_list, replace=True)
        print(num_node)
        num_cluster = np.random.choice(cluster_list, replace=True)
        adjacency_matrix,labels_vector,G = g_obj.clustered_random_graph(num_node,num_cluster,pin,pout)
        num_edge = G.numberOfEdges()

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
    information["max_num_label"] = 5
    information["min_num_label"] = 1
    graph_list.append(information)


    path = savepath + "crg_{}.pkl".format(pin)

    with open(path, "wb") as f:
        pickle.dump(graph_list, f)








