import numpy as np

class KMeans():
  def __init__(self, initial_clusters, data):
    self.clusters = initial_clusters
    self.data = data
    self.centers = None
    self.update_centers(self.clusters)
  
  def update_centers(self, clusters):
    centers_dict = {}
    for cluster in clusters.values():
      center = []
      cluster_data = [self.data[i] for i in cluster]
      cluster_data = np.transpose(cluster_data)
      for column in cluster_data:
        center.append(column.mean())
      cluster_num = list(clusters.keys())[list(clusters.values()).index(cluster)]
      centers_dict[cluster_num] = center
    self.centers = centers_dict
  
  def find_closest_center(self, point):
    closest_center = (0,99999) #(center, distance)
    for center in self.centers:
      distance = np.linalg.norm(np.array(point)-np.array(self.centers[center]))
      if distance < closest_center[1]:
        closest_center = (center, distance)
    return closest_center[0]

  def update_clusters_once(self):
    new_clusters = {}
    for point_index in range(len(self.data)):
      center = self.find_closest_center(self.data[point_index])
      try:
        new_clusters[center] += [point_index]
      except:
        new_clusters[center] = [point_index]
    self.clusters = new_clusters

  def run(self):
    prev_clusters = self.clusters.copy()
    self.update_clusters_once()
    self.update_centers(self.clusters)
    while self.clusters != prev_clusters:
      prev_clusters = self.clusters.copy()
      self.update_clusters_once()
      self.update_centers(self.clusters)
