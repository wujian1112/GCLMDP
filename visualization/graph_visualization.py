"""
Copyright@ Jian Wu,wujian1112@126.com,2022. If use or build on the code, please cite it at
URL https://github.com/wujian1112/DLMDP
"""
import networkx as nx
import matplotlib.pyplot as plt

class visal_graph(object):

    def __init__(self):
        super(visal_graph, self).__init__()
        pass

    def graph_from_nx_plot(self,G):
        """

        :param G: networkx graph
        :return: plot
        """
        pos = nx.kamada_kawai_layout(G)
        nx.draw(G, pos, node_size=200, linewidths=0, width=1, edge_color='k',with_labels = True)
        plt.title('Graph', fontsize='xx-large', fontweight='heavy')
        plt.show()

    def graph_from_numpy_plot(self,sparse_A):
        """
        :param sparse_A:  scipy_sparse_matrix
        :return: plot
        """
        G = nx.from_scipy_sparse_matrix(sparse_A)
        pos = nx.kamada_kawai_layout(G)
        nx.draw(G, pos, node_size=50, linewidths=0, width=0.5, edge_color='k',with_labels = False)
        plt.title('Graph', fontsize='xx-large', fontweight='heavy')
        plt.show()

