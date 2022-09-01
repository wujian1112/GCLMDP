
"""
Copyright@ Jian Wu,wujian1112@126.com,2022. If use or build on the code, please cite it at
URL https://github.com/wujian1112/DLMDP
"""
import networkx as nx
import networkit as nk
from networkit import generators as gen
from DLMDP.operation import matrix

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

        G = nx.random_powerlaw_tree(n, gamma=gamma, seed=seed, tries=tries)
        t = nx.is_connected(G)
        while not t:
            G = nx.G = nx.random_powerlaw_tree(n, gamma=gamma, seed=seed, tries=tries)
            t = nx.is_connected(G)
        # A = nx.adjacency_matrix(G)
        # row = torch.tensor(A.tocoo().row).reshape(-1, 1)
        # col = torch.tensor(A.tocoo().col).reshape(-1, 1)
        # data = torch.tensor(A.tocoo().data).reshape(-1, 1)
        # A = torch.cat([row, col, data], dim=1)
        return G, t

    # networkit random graph
    def clustered_random_graph(self,num_nodes,num_clusters,pin,pout):

        """
        :param num_nodes:  int,number of nodes
        :param num_clusters: int,number of clusters
        :param pin: float,intra-cluster edge probability
        :param pout: float, inter-cluster edge probability
        :return: scipy_sparse_matrix --adjacency matrix ,the generated ground truth communities --label
        """

        adj_obj = matrix.matrix_operation()
        erg = gen.ClusteredRandomGraphGenerator(num_nodes,num_clusters,pin,pout)
        # Run algorithm
        G = erg.generate()
        cc = nk.components.ConnectedComponents(G)
        cc.run()
        num = cc.numberOfComponents()
        while num>1 or num==0:
            erg = gen.ClusteredRandomGraphGenerator(num_nodes, num_clusters, pin, pout)
            # Run algorithm
            G = erg.generate()
            cc = nk.components.ConnectedComponents(G)
            cc.run()
            num = cc.numberOfComponents()
        partition = erg.getCommunities().getVector()
        A = adj_obj.adjacency_matrix_nk(G)
        return A,partition,G

