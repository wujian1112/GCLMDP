from models_for_data import pre_process_data as ppd
import networkx as nx

d =6
n = 10
obj = ppd.pre_process()
g = obj.generate(d,n)
print(g)
c = nx.clustering(g, nodes=None, weight=None)
print(c)