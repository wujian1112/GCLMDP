
"""
Copyright@ wujian1112@126.com,2022. If use or build on the code, please cite it at
URL https://github.com/wujian1112/DLMDP
"""

import networkx as nx
import numpy as np
from scipy import sparse
import scipy.io as io
import torch
'''
func: text_save(filename, data)
func: random_regular_graph(d, n, seed=None)
func: fast_gnp_random_graph(n, p, seed=None)
func: gnm_random_graph(n, m, seed=None)
f
'''


def random_regular_graph(d, n, seed=None):
    # d :degree of nodes
    # n : number of nodes
    G = nx.random_regular_graph(d, n, seed=None)
    t = nx.is_connected(G)
    while not t:
        G = nx.random_regular_graph(d, n, seed=None)
        t = nx.is_connected(G)
    A= nx.adjacency_matrix(G)
    # row = torch.tensor(A.tocoo().row).reshape(-1, 1)
    # col = torch.tensor(A.tocoo().col).reshape(-1, 1)
    # data = torch.tensor(A.tocoo().data).reshape(-1, 1)
    # A = torch.cat([row, col, data], dim=1)
    return A.todense(),t


def fast_gnp_random_graph(n, p, seed=None):
    # ｎ：　number of nodes
    # p: prob for each edge
    G = nx. fast_gnp_random_graph(n, p, seed=None, directed=False)
    t = nx.is_connected(G)
    while not t:
        G = nx.fast_gnp_random_graph(n, p, seed=None, directed=False)
        t = nx.is_connected(G)
    A = nx.adjacency_matrix(G)
    row = torch.tensor(A.tocoo().row).reshape(-1, 1)
    col = torch.tensor(A.tocoo().col).reshape(-1, 1)
    data = torch.tensor(A.tocoo().data).reshape(-1, 1)
    A = torch.cat([row, col, data], dim=1)
    return A,t


def gnm_random_graphs(n, m, seed=None):
    # ｎ：　number of nodes
    # m: number of edges
    G = nx. gnm_random_graph(n, m, seed=None, directed=False)
    t = nx.is_connected(G)

    while not t:

        G = nx.gnm_random_graph(n, m, seed=None, directed=False)
        t = nx.is_connected(G)

    A = nx.adjacency_matrix(G)
    row = torch.tensor(A.tocoo().row).reshape(-1, 1)
    col = torch.tensor(A.tocoo().col).reshape(-1, 1)
    data = torch.tensor(A.tocoo().data).reshape(-1, 1)
    A = torch.cat([row, col, data], dim=1)
    return A,t


def connected_watts_strogatz_graph(n, k, p, tries=100, seed=None):
    # ｎ：　number of nodes
    # k: Each node is joined with its k nearest neighbors in a ring topology.
    # p: The probability of rewiring each edge
    G = nx. connected_watts_strogatz_graph(n, k, p, tries=100, seed=None)
    t = nx.is_connected(G)

    while not t:

        G = nx.connected_watts_strogatz_graph(n, k, p, tries=100, seed=None)
        t = nx.is_connected(G)
    A = nx.adjacency_matrix(G)
    row = torch.tensor(A.tocoo().row).reshape(-1, 1)
    col = torch.tensor(A.tocoo().col).reshape(-1, 1)
    data = torch.tensor(A.tocoo().data).reshape(-1, 1)
    A = torch.cat([row, col, data], dim=1)
    return A,t

def powerlaw_cluster_graph(n, m, p, seed=None):
    # ｎ：　number of nodes
    # m: the number of random edges to add for each new node.
    # p: Probability of adding a triangle after adding a random edge
    G = nx. powerlaw_cluster_graph(n, m, p, seed=None)
    t = nx.is_connected(G)
    while not t:
        G = nx.powerlaw_cluster_graph(n, m, p, seed=None)
        t = nx.is_connected(G)
    A = nx.adjacency_matrix(G)
    row = torch.tensor(A.tocoo().row).reshape(-1, 1)
    col = torch.tensor(A.tocoo().col).reshape(-1, 1)
    data = torch.tensor(A.tocoo().data).reshape(-1, 1)
    A = torch.cat([row, col, data], dim=1)
    return A,t

def random_powerlaw_tree(n, tries,gamma=3, seed=None):
    # ｎ：　number of nodes
    # gamma : Exponent of the power law.
    # tries: Number of attempts to adjust the sequence to make it a tree.
    G = nx. random_powerlaw_tree(n, gamma=3, seed=None, tries=tries)
    t = nx.is_connected(G)
    while not t:
        G = nx.G = nx. random_powerlaw_tree(n, gamma=3, seed=None, tries=tries)
        t = nx.is_connected(G)
    A = nx.adjacency_matrix(G)
    # row = torch.tensor(A.tocoo().row).reshape(-1, 1)
    # col = torch.tensor(A.tocoo().col).reshape(-1, 1)
    # data = torch.tensor(A.tocoo().data).reshape(-1, 1)
    # A = torch.cat([row, col, data], dim=1)
    return A.todense(),t




def text_save(filename, data):
    # 稀疏邻接矩阵的列表表示.
    data = data.tolist()
    file= open(filename, 'w')
    file.close()
    file = open(filename,'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
        s = s.replace("'",'').replace(',','') +'\n'   #去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("save successful")

