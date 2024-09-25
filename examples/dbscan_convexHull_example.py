import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

"""
Tools used in this code and their purpose:

1. **DBSCAN (from sklearn.cluster)**:
   - DBSCAN (Density-Based Spatial Clustering of Applications with Noise) is used to find clusters in the dataset. 
   - It identifies clusters based on a neighborhood distance (`eps`) and a minimum number of points (`min_samples`).
   - Noise points are labeled as `-1`, while the clustered points are given specific labels.

2. **ConvexHull (from scipy.spatial)**:
   - ConvexHull is a computational geometry tool that finds the smallest convex polygon (or hull) that can enclose a set of points.
   - The vertices of the convex hull are used to approximate the minimum enclosing circle, as they represent the outermost points of the clusters.

3. **Matplotlib (for visualization)**:
   - Matplotlib is a plotting library used to visualize the data points, clusters, and the enclosing circle.
   - `plt.scatter()` is used to display the data points, and `plt.Circle()` is used to draw the minimum enclosing circle around the clusters.

Steps Overview:
1. DBSCAN is applied to the data points to identify clusters.
2. Clustered points (excluding noise) are extracted for further analysis.
3. The convex hull of the clustered points is computed, and an approximate center of the enclosing circle is calculated as the mean of the hull points.
4. The radius of the enclosing circle is computed as the maximum distance from the center to any point on the convex hull.
5. The clusters and the enclosing circle are visualized using matplotlib, showing how the circle covers all the clustered points.
"""

# Sample input data points
x = np.array([(1, 2), (0, 1), (1, 3), (10, 10), (9, 9), (10, 11)])

# Step 1: Run DBSCAN
db = DBSCAN(eps=1.5, min_samples=2).fit(x)
labels = db.labels_

# Step 2: Extract points that belong to clusters (excluding noise)
cluster_points = x[labels != -1]  # Ignoring noise points (-1 label)

# Step 3: Function to calculate minimum enclosing circle
def minimum_enclosing_circle(points):
    hull = ConvexHull(points)
    hull_points = points[hull.vertices]
    
    # Mean of the hull vertices can serve as a center approximation
    center = np.mean(hull_points, axis=0)
    
    # Calculate the radius as the maximum distance from the center to any hull point
    radius = np.max(np.linalg.norm(hull_points - center, axis=1))
    
    return center, radius

# Calculate minimum enclosing circle for the cluster points
center, radius = minimum_enclosing_circle(cluster_points)

# Step 4: Visualization
fig, ax = plt.subplots()

# Plot data points
ax.scatter(x[:, 0], x[:, 1], c=labels, cmap='viridis', marker='o')

# Draw minimum enclosing circle
circle = plt.Circle(center, radius, color='r', fill=False, linestyle='--')
ax.add_patch(circle)

# Plot center of the circle
ax.plot(center[0], center[1], 'ro')

# Add labels and show plot
ax.set_title('DBSCAN Clusters with Enclosing Circle')
ax.set_aspect('equal')
plt.show()

print("Center of enclosing circle:", center)
print("Radius of enclosing circle:", radius)
