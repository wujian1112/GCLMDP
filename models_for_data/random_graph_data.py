

"""
Copyright@ wujian1112@126.com,2022. If use or build on the code, please cite it
"""
import networkx as nx

class random_graph(object):

    def __init__(self):
        super(random_graph, self).__init__()
        pass

    def random_powerlaw_tree(self,n, tries, gamma=3, seed=None):
        """
        :param n: number of nodes
        :param tries: Number of attempts to adjust the sequence to make it a tree.
        :param gamma: Exponent of the power law.
        :param seed:
        :return: G the networkx graph
        """

        G = nx.random_powerlaw_tree(n, gamma=3, seed=None, tries=tries)
        t = nx.is_connected(G)
        while not t:
            G = nx.G = nx.random_powerlaw_tree(n, gamma=3, seed=None, tries=tries)
            t = nx.is_connected(G)
        # A = nx.adjacency_matrix(G)
        # row = torch.tensor(A.tocoo().row).reshape(-1, 1)
        # col = torch.tensor(A.tocoo().col).reshape(-1, 1)
        # data = torch.tensor(A.tocoo().data).reshape(-1, 1)
        # A = torch.cat([row, col, data], dim=1)
        return G, t