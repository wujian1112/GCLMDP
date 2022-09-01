
import networkx as nx
from networkx.algorithms import community, node_classification


class pre_process(object):

    def __init__(self):
        super(pre_process, self).__init__()
        pass



    def community_decttion_1(self,G):
        comm = community.louvain_communities(G)
        return comm

    def community_decttion_2(self,G):
        communities_generator = community.girvan_newman(G)
        next_level_communities = next(communities_generator)

        return sorted(map(sorted, next_level_communities))



    def rank(self,G):
        pr = nx.pagerank(G, alpha=0.9)
        return pr

    def centrallity_1(self,G):
        return nx.degree_centrality(G)

    def centrallity_2(self,G):
        return nx.eigenvector_centrality(G, max_iter=100, tol=1e-06, nstart=None, weight=None)

    def centrallity_3(self,G):
        return nx.load_centrality(G, v=None, cutoff=None, normalized=True, weight=None)

    def centrallity_4(self,G):
        return nx.betweenness_centrality(G, k=None, normalized=True, weight=None, endpoints=False, seed=None)








