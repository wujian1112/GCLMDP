
"""
Copyright@ Jian Wu,wujian1112@126.com,2022. If use or build on the code, please cite it at
URL https://github.com/wujian1112/DLMDP
"""
"""
To generate barbell_graph saved in 'data/barbell_graph/'
"""

from models_for_data import random_graph_data as rgd
import numpy as np
import pickle
import os
import random

# save data
savepath= 'data/barbell_graph/'
a= os.path.exists(savepath)
if not a:
    os.makedirs(savepath)

# data parameters
m1_list = list(range(3,50))
random.shuffle(m1_list)
m2_list = list(range(1,20))
random.shuffle(m2_list)

# generate data
information = dict()
graph_list = []
node_total = 0
edge_total = 0
node_ave = 0
edge_ave = 0
num_graph = 500

for i in range(num_graph):
    graph = dict()
    g_obj = rgd.random_graph()
    print('graph_i = ',  i)

    m1 = np.random.choice(m1_list, replace=True)
    m2 = np.random.choice(m2_list, replace=True)
    adjacency_matrix,labels_vector,G = g_obj.barbell_graph(m1, m2, create_using=None)
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

path = savepath + "bg.pkl"

with open(path, "wb") as f:
    pickle.dump(graph_list, f)








