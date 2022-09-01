"""
Copyright@ Jian Wu,wujian1112@126.com,2022. If use or build on the code, please cite it at
URL https://github.com/wujian1112/DLMDP
"""

import networkx as nx
import networkit as nk
from networkit import algebraic as alge



class matrix_operation(object):

    def __init__(self):
        super(matrix_operation, self).__init__()
        pass

    def adjacency_matrix_nk(self, G):

        """
        :param G: networkit graph
        :return: sparse adjacency matrix
        """
        return alge.adjacencyMatrix(G, matrixType='sparse')




