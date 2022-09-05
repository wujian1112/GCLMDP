"""
load data to compute the statistical characteristics
"""

import pickle
from visualization import graph_visualization as gv

plotobj = gv.visal_graph()
flag = 5  # 0: crp, 1: gnp, 2: rpt, 3: rt, 4; rc, 5：bg

if flag==0:
    # ///////////////////////////////////////////////////////
    # (1)load data of clustered_random_graph
    pin_list = [0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
    savepath= 'data/clustered_random_graph/'

    labels = set()
    ave_nodes = 0
    ave_edges = 0
    graphs = 0
    for i,p in enumerate(pin_list):
        print(i,p)
        path = savepath + "crg_{}.pkl".format(p)
        my_data = pickle.load(open(path, 'rb'))

        ave_nodes += my_data[-1]['node_ave']
        ave_edges += my_data[-1]['edge_ave']
        graphs += my_data[-1]['num_graph']
        for j in range(my_data[-1]['num_graph']):
            labels = labels.union(my_data[j]['labels'])
    ave_nodes = ave_nodes/len(pin_list)
    ave_edges =ave_edges/ len(pin_list)
    print('crp: ','ave_nodes =',ave_nodes,'ave_edges=',ave_edges,'graphs=',graphs,'labels=',labels)
elif flag==1:
    # (2)load data of gnp_random_graph
    pin_list = [0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
    savepath= 'data/gnp_random_graph/'

    labels = set()
    ave_nodes = 0
    ave_edges = 0
    graphs = 0
    for i,p in enumerate(pin_list):
        print(i,p)
        path = savepath + "gnp_{}.pkl".format(p)
        my_data = pickle.load(open(path, 'rb'))
        ave_nodes += my_data[-1]['node_ave']
        ave_edges += my_data[-1]['edge_ave']
        graphs += my_data[-1]['num_graph']
        for j in range(my_data[-1]['num_graph']):
            labels = labels.union(my_data[j]['labels'])
    ave_nodes = ave_nodes/len(pin_list)
    ave_edges =ave_edges/ len(pin_list)
    print('gnp: ','ave_nodes =',ave_nodes,'ave_edges=',ave_edges,'graphs=',graphs,'labels=',labels)

elif flag==2:

    # (3)load data of random_powerlaw_tree
    savepath= 'data/random_powerlaw_tree/'
    path = savepath + "rpt.pkl"
    my_data = pickle.load(open(path, 'rb'))

    # compute the number of labels for nodes
    labels = set()
    for i in range(my_data[-1]['num_graph']):
        labels = labels.union(my_data[i]['labels'])

    # compute properties for graphs
    ave_nodes = my_data[-1]['node_ave']
    ave_edges = my_data[-1]['edge_ave']
    num_graph = my_data[-1]['num_graph']
    print('rpt: ','ave_nodes =',ave_nodes,'ave_edges=',ave_edges,'graphs=',num_graph,'labels=',labels)

elif flag==3:

    # (4)load data of random_tree
    savepath= 'data/random_tree/'
    path = savepath + "rt.pkl"
    my_data = pickle.load(open(path, 'rb'))

    # compute the number of labels for nodes
    labels = set()
    for i in range(my_data[-1]['num_graph']):
        labels = labels.union(my_data[i]['labels'])

    # compute properties for graphs
    ave_nodes = my_data[-1]['node_ave']
    ave_edges = my_data[-1]['edge_ave']
    num_graph = my_data[-1]['num_graph']
    print('rt: ','ave_nodes =',ave_nodes,'ave_edges=',ave_edges,'graphs=',num_graph,'labels=',labels)
elif flag == 4:

    # (5)load data of ring_of_cliques
    savepath= 'data/ring_of_cliques/'
    path = savepath + "rc.pkl"
    my_data = pickle.load(open(path, 'rb'))

    # compute the number of labels for nodes
    labels = set()
    for i in range(my_data[-1]['num_graph']):
        labels = labels.union(my_data[i]['labels'])

    # compute properties for graphs
    ave_nodes = my_data[-1]['node_ave']
    ave_edges = my_data[-1]['edge_ave']
    num_graph = my_data[-1]['num_graph']
    print('rc: ','ave_nodes =',ave_nodes,'ave_edges=',ave_edges,'graphs=',num_graph,'labels=',labels)

elif flag == 5:

    # (6)load data of barbell_graph
    savepath= 'data/barbell_graph/'
    path = savepath + "bg.pkl"
    my_data = pickle.load(open(path, 'rb'))

    # compute the number of labels for nodes
    labels = set()
    for i in range(my_data[-1]['num_graph']):
        labels = labels.union(my_data[i]['labels'])

    # compute properties for graphs
    ave_nodes = my_data[-1]['node_ave']
    ave_edges = my_data[-1]['edge_ave']
    num_graph = my_data[-1]['num_graph']
    print('bg: ','ave_nodes =',ave_nodes,'ave_edges=',ave_edges,'graphs=',num_graph,'labels=',labels)

# ////////////////////////////////////////////
# graph view and print
# my_data = pickle.load(open(path, 'rb'))
# print(my_data[-1])
# plotobj.graph_from_numpy_plot(my_data[300]['adj'])