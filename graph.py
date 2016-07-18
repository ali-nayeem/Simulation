import igraph
import numpy as np

dataset = 'M0'
nodes = 30
fileName = 'M0Distances.txt'

node_names = range(0,nodes) 

A = np.genfromtxt(fileName)
A = np.nan_to_num(A) 

# Create graph, A.astype(bool).tolist() or (A / A).tolist() can also be used.
g = igraph.Graph.Adjacency((A > 0).tolist(),mode=igraph.ADJ_UNDIRECTED)

# Add edge weights and node labels.
g.es['weight'] = A[(np.triu(A)).nonzero()]
g.es['weight'] = [int(i) for i in g.es['weight']]
g.vs['label'] = node_names  # or a.index/a.columns
g.es['label'] = g.es['weight']
layout = g.layout("kk")
igraph.plot(g, dataset+"_fig.pdf",layout=layout)
writeFile = open(dataset+'_edgelist.txt', 'w')
writeFile.write('#src dest weight' )
for e in g.es:
    line = '\n'+str(e.tuple[0]) + ' ' +str(e.tuple[1]) + ' ' + str(e["weight"])
    writeFile.write(line)
writeFile.close()
   