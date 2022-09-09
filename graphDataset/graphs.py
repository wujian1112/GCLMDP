"""
Copyright@ Jian Wu,wujian1112@126.com,2022. If use or build on the code, please cite it at
URL https://github.com/wujian1112/DLMDP
"""
import networkx as nx
from networkx.algorithms import community
import networkit as nk
from networkit import generators as gen
# from networkit import community as nkc
from DLMDP.operation import matrix

import torch as th

class graph(object):

    def __init__(self):
        super(graph, self).__init__()
        pass

    def starGraph(self,leaf_node_num):
        g = nx.star_graph(leaf_node_num, create_using=None)
        return g

