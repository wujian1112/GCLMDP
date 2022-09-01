
import networkit as nk
from operation import matrix

n=10
k=3
pIntra = 0.5
pInter =0.2


aobj = matrix.matrix_operation()

# Initalize algorithm

erg = nk.generators.ClusteredRandomGraphGenerator(10,3,0.5,0.2)
# Run algorithm
G = erg.generate()
A = aobj.adjacency_matrix_nk(G)
print(A)


print(G.numberOfNodes(), G.numberOfEdges())
partition = erg.getCommunities().getVector()
print(partition)





