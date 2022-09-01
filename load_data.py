import pickle
from visualization import graph_visualization as gv

plotobj = gv.visal_graph()

pin_list = [0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
savepath= 'data/clustered_random_graph/'
path = savepath + "crg_{}.pkl".format(0.9)

my_data = pickle.load(open(path, 'rb'))

# # graph view
print(my_data[-2])
plotobj.graph_from_numpy_plot(my_data[-2]['adj'])