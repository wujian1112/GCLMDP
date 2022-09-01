
"""
Copyright@ Jian Wu,wujian1112@126.com,2022. If use or build on the code, please cite it at
URL https://github.com/wujian1112/DLMDP
"""
import networkx as nx
from networkx.algorithms import community
import networkit as nk
from networkit import generators as gen
from networkit import community as nkc
from DLMDP.operation import matrix

class random_graph(object):

    def __init__(self):
        super(random_graph, self).__init__()
        pass

    # networkx random graph
    def random_tree(self,n, seed=None, create_using=None):
        """

        :param num_cliques:
        :param clique_size:
        :return: A, label,G
        """
        G = nx.random_tree(n, seed=None, create_using=None)
        t = nx.is_connected(G)
        while not t:
            G = nx.random_tree(n, seed=None, create_using=None)
            t = nx.is_connected(G)

        A = nx.adjacency_matrix(G)
        communities_generator = community.girvan_newman(G)
        next_level_communities = next(communities_generator)
        partition = sorted(map(sorted, next_level_communities))
        label = [0]*n

        for i in range(len(partition)):
            for j in range(n):
                if j in partition[i]:
                    label[j] = i

        return A, label,G

    def barbell_graph(self,m1, m2, create_using=None):
        """

        :param num_cliques:
        :param clique_size:
        :return: A, label,G
        """
        G = nx.barbell_graph(m1, m2, create_using=None)
        t = nx.is_connected(G)
        while not t:
            G = nx.barbell_graph(m1, m2, create_using=None)
            t = nx.is_connected(G)
        n = G.number_of_nodes()
        A = nx.adjacency_matrix(G)
        communities_generator = community.girvan_newman(G)
        next_level_communities = next(communities_generator)
        partition = sorted(map(sorted, next_level_communities))
        label = [0]*n

        for i in range(len(partition)):
            for j in range(n):
                if j in partition[i]:
                    label[j] = i

        return A, label,G

    def ring_cliques(self,num_cliques, clique_size):
        """

        :param num_cliques:
        :param clique_size:
        :return: A, label,G
        """
        G = nx.ring_of_cliques(num_cliques, clique_size)
        t = nx.is_connected(G)
        while not t:
            G = nx.ring_of_cliques(num_cliques, clique_size)
            t = nx.is_connected(G)
        n = G.number_of_nodes()
        A = nx.adjacency_matrix(G)
        communities_generator = community.girvan_newman(G)
        next_level_communities = next(communities_generator)
        partition = sorted(map(sorted, next_level_communities))
        label = [0]*n

        for i in range(len(partition)):
            for j in range(n):
                if j in partition[i]:
                    label[j] = i

        return A, label,G

    def gnp_random_graph(self,n, p, seed=None):
        """

        :param n: number of nodes
        :param p: probability for edge existing
        :param seed:
        :return: A, label,G
        """
        G = nx.gnp_random_graph(n, p, seed=seed, directed=False)
        t = nx.is_connected(G)
        while not t:
            G = nx.fast_gnp_random_graph(n, p, seed=seed, directed=False)
            t = nx.is_connected(G)
        A = nx.adjacency_matrix(G)
        communities_generator = community.girvan_newman(G)
        next_level_communities = next(communities_generator)
        partition = sorted(map(sorted, next_level_communities))
        label = [0]*n

        for i in range(len(partition)):
            for j in range(n):
                if j in partition[i]:
                    label[j] = i

        return A, label,G

    def random_powerlaw_tree(self, n, tries, gamma=3,seed=None):
        """
        :param gamma:
        :param tries:
        :param seed:
        :return:
        """
        flag = True
        try:
            G = nx.random_powerlaw_tree(n, gamma=gamma, seed=None, tries=tries)
        except:
            flag=False

        while not flag:
            try:
                G = nx.random_powerlaw_tree(n, gamma=gamma, seed=None, tries=tries)
            except:
                flag = False
        t = nx.is_connected(G)
        while not t:
            flag = True
            try:
                G = nx.random_powerlaw_tree(n, gamma=gamma, seed=None, tries=tries)
            except:
                flag = False

            while not flag:
                try:
                    G = nx.random_powerlaw_tree(n, gamma=gamma, seed=None, tries=tries)
                except:
                    flag = False
            t = nx.is_connected(G)

        A = nx.adjacency_matrix(G)
        communities_generator = community.girvan_newman(G)
        next_level_communities = next(communities_generator)
        partition = sorted(map(sorted, next_level_communities))
        label = [0]*n

        for i in range(len(partition)):
            for j in range(n):
                if j in partition[i]:
                    label[j] = i

        return A, label,G


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



