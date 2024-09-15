import numpy as np

from sklearn import metrics
from sklearn.cluster import DBSCAN

x = [(1,2), (0,1), (1,3), (10,10)]

db = DBSCAN(eps=1, min_samples=2).fit(x)
labels = db.labels_

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)

print("Estimated number of clusters: %d" % n_clusters_)
print("Estimated number of noise points: %d" % n_noise_)