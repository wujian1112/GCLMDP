
import networkx as nx
import torch


class pre_process(object):

    def __init__(self):
        super(pre_process, self).__init__()
        pass



    def generate(self,d,n):
        G = nx.random_regular_graph(d, n, seed=None)
        t = nx.is_connected(G)
        while not t:
            G = nx.random_regular_graph(d, n, seed=None)
            t = nx.is_connected(G)
        return G





