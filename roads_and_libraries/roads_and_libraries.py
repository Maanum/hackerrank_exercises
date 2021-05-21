#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#

PROBLEM_INPUT = [
    [3, 2, 1, [[1, 2], [3, 1], [2, 3]]],
    [6, 2, 5, [[1, 3], [3, 4], [2, 4], [1, 2], [2, 3], [5, 6]]],
    [5, 6, 1, [[1, 2], [1, 3], [1, 4]]],
]


def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib < c_road:
        return c_lib * n

    networks = []

    city_graph = {i : [j for j in cities if i in j] for i in range(1, n + 1)}
    for key in city_graph:
        city_graph[key] = set([item for sublist in city_graph[key] for item in sublist])

    cities = list(city_graph.keys())

    def get_network():
        network = city_graph[cities[0]]
        cities.pop(0)
        def find_neighbors():
            diff = network.intersection(set(cities))
            if not diff:
                return
            else:
                for city in diff:
                    network.update(city_graph[city])
                    cities.remove(city)
                find_neighbors()
        find_neighbors()
        networks.append(network)
        if len(cities) > 0:
            get_network()

    get_network()
    cost_roads = c_road * (n - len(networks))
    cost_libraries = c_lib * len(networks)

    return cost_roads + cost_libraries

if __name__ == '__main__':
    q = PROBLEM_INPUT

    for q_itr in q:
        n = int(q_itr[0])
        c_lib = int(q_itr[1])
        c_road = int(q_itr[2])
        cities = q_itr[3]
        result = roadsAndLibraries(n, c_lib, c_road, cities)
        print(f'result = {result}')
