import pickle
from visualization import graph_visualization as gv

plotobj = gv.visal_graph()

# (1)load data of clustered_random_graph
# pin_list = [0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
# savepath= 'data/clustered_random_graph/'
# path = savepath + "crg_{}.pkl".format(0.2)

# (2)load data of gnp_random_graph
# savepath= 'data/gnp_random_graph/'
# path = savepath + "gnp_{}.pkl".format(0.3)

# (3)load data of random_tree
# savepath= 'data/random_tree/'
# path = savepath + "rt.pkl"

# (4)load data of random_powerlaw_tree
# savepath= 'data/random_powerlaw_tree/'
# path = savepath + "rpt.pkl"

# (5)load data of ring_of_cliques
savepath= 'data/ring_of_cliques/'
path = savepath + "rc.pkl"


my_data = pickle.load(open(path, 'rb'))

# # graph view
print(my_data[-1])

plotobj.graph_from_numpy_plot(my_data[90]['adj'])