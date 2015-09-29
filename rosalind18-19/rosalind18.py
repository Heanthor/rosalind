from sys import maxint
from math import sqrt

filename = "rosalind_ba8b.txt"


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
            tmp = float(distance)
            min_distance = distance
    return tmp


def squared_error_distortion(m, centers, data):
    s = 0
    n = len(data)

    for pt in data:
        s += (nearest_center(m, pt, centers))**2
    return (1.0/n) * s

with open(filename, 'r') as f:
    k, m = f.readline().strip().split(" ")
    centers = []
    points = []

    while True:
        line = f.readline().strip()

        if '-' in line:
            break
        centers.append(line.split(" "))

    while True:
        line = f.readline().strip()

        if not line:
            break

        points.append(line.split(" "))

    print squared_error_distortion(m, centers, points)
