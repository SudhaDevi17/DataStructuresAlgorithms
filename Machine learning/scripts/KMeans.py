import random
import numpy as np
from dataclasses import dataclass, field

@dataclass
class Centroid:
    location: np.array = None
    members: list = field(default_factory = list)

    def __post_init__(self):
        self.location = np.array(self.location)
    def distance(self, point : np.array, measure= 'manhattan'):
        point = np.array(point)
        assert point.ndim == self.location.ndim, 'Feature space and centroid space mismatch'

        if measure == 'manhattan':
            order =1
        elif measure == 'euclidean':
            order = 2
        else:
            raise ValueError('Measure must be manhattan or euclidean')
        return np.linalg.norm(point - self.location , ord= order)

    def reset_members(self):
        self.members = [ ]

    def add_members(self, member) :
        self.members.append(member)

    def compute_location(self):
        self.location = np.mean(np.array(self.members), axis = 0 )

def reset_centroid_members(centroids):
    for c in centroids:
        c.reset_members()
def compute_closest_centroid(centroid , feats):
    dists = [c.distance(feats) for c in centroid]
    closest_centroid = centroid[np.argmin(dists)]
    return closest_centroid

def update_centroids(centroids):
    for c in centroids:
        c.compute_location()
def get_k_means(user_feature_map, num_features_per_user, k):
    # Don't change the following two lines of code.
    random.seed(42)
    # Gets the inital users, to be used as centroids.
    inital_centroid_users = random.sample(sorted(list(user_feature_map.keys())), k)

    centroids = [Centroid(user_feature_map[user]) for user in inital_centroid_users]

    for i in range(10):
        reset_centroid_members(centroids)

        for user, feat in user_feature_map.items():
            closest_centroid = compute_closest_centroid(centroids, feat)
            closest_centroid.add_members(feat)
        update_centroids(centroids)

    return [list(c.location) for c in centroids]
