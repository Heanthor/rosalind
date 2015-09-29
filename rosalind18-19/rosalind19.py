from random import sample
from math import sqrt
from sys import maxint
from collections import defaultdict
from ast import literal_eval

filename = "ex19.txt"


def calculate_distance(m, p1, p2):
    tmp = 0.0

    for i in range(m):
        tmp += (float(p1[i]) - float(p2[i]))**2
    return sqrt(tmp)


def nearest_center(m, point, centers):
    min_distance = maxint
    tmp = -1

    for center in centers:
        distance = calculate_distance(int(m), point, center)
        if distance < min_distance:
            tmp = center
            min_distance = distance
    return tmp


def arbitrary_points(k, dataset):
    to_return = []
    indices = sample(range(len(dataset)), k)

    for i in range(len(indices)):
        to_return.append(dataset[indices[i]])
    return to_return


def center_of_gravity(m, set_of_points):
    to_return = []
    n = len(set_of_points)

    for i in range(m):
        tmp = 0.0
        for point in set_of_points:
            tmp += float(point[i])
        to_return.append(tmp / n)

    return to_return


def centers_to_clusters(m, centers, data):
    clusters = defaultdict(list)

    for pt in data:
        closest_center = nearest_center(m, pt, centers)
        clusters[str(closest_center)].append(pt)
    return clusters


def clusters_to_centers(m, clusters_hash):
    new_hash = defaultdict(list)

    for center, points in clusters_hash.items():
        cog = center_of_gravity(m, points)
        new_hash[str(cog)] = points

    return new_hash


with open(filename, 'r') as f:
    k, m = f.readline().strip().split(" ")
    data = []

    while True:
        line = f.readline().strip()

        if not line:
            break

        data.append(line.split(" "))
    print center_of_gravity(int(m), data)
    ap = arbitrary_points(int(k), data)
    print ap
    c = centers_to_clusters(int(m), ap, data)
    print c
    print clusters_to_centers(int(m), c)
