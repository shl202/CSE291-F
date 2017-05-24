#!/user/bin/env python

from sklearn.cluster import KMeans
import numpy as np
import networkx as nx
import sys

fread = str(sys.argv[1])
fwrite = open(str(sys.argv[2]), "w")
clusters = int(sys.argv[3])

with open(fread) as f:
	emb = f.readlines()

header = emb[0]
data = np.array([ [ float(entry) for entry in line.split()] for line in emb[1:]])
nodes = data[:, 0]
X = data[:, 1:]

kmeans = KMeans(n_clusters=clusters, random_state=0).fit(X)
labels = kmeans.labels_

for i, node in enumerate(nodes):	
	fwrite.write(str(int(node)) + '  '  + str(labels[i]) +'\n')
