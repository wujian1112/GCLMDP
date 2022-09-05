from DLMDP.beiyoong import pre_process_data as ppd
from models_for_data import random_graph_data as rgd
import networkx as nx

from visualization import graph_visualization as gv

# object for graphs
gobj = rgd.random_graph()
process = ppd.pre_process()
plotobj = gv.visal_graph()

tries =500000
n = 20
g,t = gobj.random_powerlaw_tree(n, tries, gamma=2, seed=123)
print(g.degree)
print(g)
c = nx.clustering(g, nodes=None, weight=None)
print(c)
# d = community.label_propagation_communities(g)
d = process.community_decttion_2(g)

# d = process.centrallity_4(g)
print('d=',d)
plotobj.graph_plot(g)
# for i in d:
#     print(i)
