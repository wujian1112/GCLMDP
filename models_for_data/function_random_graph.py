import random_dataset as rd
import os


# /////////////////////// random graph:random_regular_graph//////////////

# d :degree of nodes
# n : number of nodes
# return sparse adjacency matrix : list
# save to .txt

savepath= './data/random_regular_graph/'
a= os.path.exists(savepath)
if not a:
    os.makedirs(savepath)

n=100
d = [2,3,5,7,8,10,15,20,25,30]

for degree in d:
    filename="regular_{}_{}.txt".format(degree,n)
    A,t = rd.random_regular_graph(degree, n, seed=None)
    print(t)
    path = savepath+filename
    rd.text_save(path, A)



# /////////////////////// random graph:fast_gnp_random_graph//////////////

# ｎ：　number of nodes
    # p: prob for each edge
# return sparse adjacency matrix : list
# save to .txt
'''
savepath= 'data/random_gnp/'
a= os.path.exists(savepath)
if not a:
    os.makedirs(savepath)

n=100
p = [0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]

for prob in p:
    filename="gnp_{}_{}.txt".format(prob,n)
    A,t = rd.fast_gnp_random_graph(n, prob, seed=None)
    print(t)
    path = savepath+filename
    rd.text_save(path, A)
'''

# /////////////////////// random graph:gnm_random_graph//////////////

# ｎ：　number of nodes
# m: number of edges
# return sparse adjacency matrix : list
# save to .txt
'''
savepath= 'data/random_gnm/'
a= os.path.exists(savepath)
if not a:
    os.makedirs(savepath)

n=100
edges = [250,300,352,410,450,520,605,650,700,800]

for m in edges:
    print(m)
    filename="gnm_{}_{}.txt".format(n,m)
    A,t = rd.gnm_random_graphs(n, m, seed=None)
    print(t)
    path = savepath+filename
    rd.text_save(path, A)
'''

# /////////////////////// random graph:connected_watts_strogatz_graph//////////////

# ｎ：　number of nodes
# k: Each node is joined with its k nearest neighbors in a ring topology.
# p: The probability of rewiring each edge
# return sparse adjacency matrix : list
# save to .txt
'''
savepath= 'data/random_watts/'
a= os.path.exists(savepath)
if not a:
    os.makedirs(savepath)

n=100
neigh= [5,11,20,30,40,55,60,75,85,90]
p = 0.5

for k in neigh:
    filename="watts_{}_{}_{}.txt".format(n,k,p)
    A,t = rd.connected_watts_strogatz_graph(n, k, p, tries=100, seed=None)
    print(t)
    path = savepath+filename
    rd.text_save(path, A)
'''

# /////////////////////// random graph:powerlaw_cluster_graph//////////////

# ｎ：　number of nodes
# k: Each node is joined with its k nearest neighbors in a ring topology.
# p: The probability of rewiring each edge
# return sparse adjacency matrix : list
# save to .txt
'''
savepath= 'data/random_cluster_graph/'
a= os.path.exists(savepath)
if not a:
    os.makedirs(savepath)

n=100
neigh= [5,11,15,20,30,40,51,62,75,80]
p = 0.5

for m in neigh:
    filename="cluster_graph_{}_{}_{}.txt".format(n,m,p)
    A,t = rd.powerlaw_cluster_graph(n, m, p, seed=None)
    print(t)
    path = savepath+filename
    rd.text_save(path, A)
'''

# /////////////////////// random graph:random_powerlaw_tree//////////////

# ｎ：　number of nodes
# k: Each node is joined with its k nearest neighbors in a ring topology.
# p: The probability of rewiring each edge
# return sparse adjacency matrix : list
# save to .txt
'''
savepath= 'data/random_random_powerlaw_tree/'
a= os.path.exists(savepath)
if not a:
    os.makedirs(savepath)

n=100
gamma=[1,2,3,4,5,6,7,8,9,10]
tries = 4000
for m in gamma:
    filename="powerlaw_tree_{}_{}.txt".format(n,m)
    A,t = rd.random_powerlaw_tree(n, tries,gamma=m, seed=None)
    print(t)
    path = savepath+filename
    rd.text_save(path, A)
'''









