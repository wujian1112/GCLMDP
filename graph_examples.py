import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from visualization import graph_visualization as gv
import pickle

fig = plt.figure()

ax1= fig.add_subplot(231)
savepath = 'data/clustered_random_graph/'
# CRP
p=0.5
path = savepath + "crg_{}.pkl".format(p)
my_data = pickle.load(open(path, 'rb'))
plotobj = gv.visal_graph()
plotobj.graph_from_numpy_plot(my_data[880]['adj'])
plt.title('(a) CRG')

ax2= fig.add_subplot(232)
# GNP
p=0.2
savepath= 'data/gnp_random_graph/'
path = savepath + "gnp_{}.pkl".format(p)
my_data = pickle.load(open(path, 'rb'))
plotobj = gv.visal_graph()
plotobj.graph_from_numpy_plot(my_data[880]['adj'])
plt.title('(b) GNP')

ax3= fig.add_subplot(233)
# RPT
savepath= 'data/random_powerlaw_tree/'
path = savepath + "rpt.pkl"
my_data = pickle.load(open(path, 'rb'))
plotobj = gv.visal_graph()
plotobj.graph_from_numpy_plot(my_data[0]['adj'])
plt.title('(c) RPT')

ax4= fig.add_subplot(234)
# RPT
savepath= 'data/random_tree/'
path = savepath + "rt.pkl"
my_data = pickle.load(open(path, 'rb'))
plotobj = gv.visal_graph()
plotobj.graph_from_numpy_plot(my_data[0]['adj'])
plt.title('(d) RT')

ax5= fig.add_subplot(235)
# RPT
savepath = 'data/ring_of_cliques/'
path = savepath + "rc.pkl"
my_data = pickle.load(open(path, 'rb'))
plotobj = gv.visal_graph()
plotobj.graph_from_numpy_plot(my_data[0]['adj'])
plt.title('(e) RC')


ax6= fig.add_subplot(236)
# RPT
savepath = 'data/barbell_graph/'
path = savepath + "bg.pkl"
my_data = pickle.load(open(path, 'rb'))
plotobj = gv.visal_graph()
plotobj.graph_from_numpy_plot(my_data[88]['adj'])
plt.title('(f) BG')
plt.show()