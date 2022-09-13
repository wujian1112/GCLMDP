
import function_tool as ft

# load star graph data
# it is selected according to the dataset
datasetname = 'crg_gnp_random_graph' # 'crg_gnp_random_graph', 'rpt_rt_tree_graph','rc_bg_graph'
graphname = 'crg_gnp_0.5' # 'crg_gnp_p' p=0.2-0.9. 'rpt_rt','rc_bg'
label_list = ['crg', 'gnp'] # ['crg', 'gnp'], ['rpt', 'rt'], ['rc', 'bg']
# location
datasavepath = 'data/{}/'.format(datasetname)
datafilename = '{}_star.pkl'.format(graphname)
path = datasavepath + datafilename

path2 = datasavepath +'{}.pkl'.format(graphname)

dataset = ft.load_data(path)
print(dataset[10])
dataset2 = ft.load_data(path2)
print(dataset2[10])

