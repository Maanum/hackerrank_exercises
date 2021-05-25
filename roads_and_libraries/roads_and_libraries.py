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


def format_line(line):
    return [int(i) for i in line.split()]


def process_input(file_name):
    with open(file_name, 'r') as reader:
        test_cases_count = int(reader.readline())
        test_cases = []
        for _ in range(test_cases_count):
            test_info = [0, 0, 0, []]
            test_info[0], connections_count, test_info[1], test_info[
                2] = format_line(reader.readline())
            for _ in range(connections_count):
                test_info[3].append(format_line(reader.readline()))

            test_cases.append(test_info)

    return test_cases


def roadsAndLibraries(n, c_lib, c_road, cities):

    if c_lib < c_road:
        return c_lib * n

    checked = set()
    not_checked = set()
    count_networks = 0

    while len(cities) > 0:
        not_checked.update(cities.pop())
        while len(not_checked) > 0:
            found_cities = set()

            for city in cities:
                if not not_checked.isdisjoint(set(city)):
                    found_cities.update(city)
            checked.update(not_checked)
            not_checked.clear()
            cities = [
                city for city in cities if found_cities.isdisjoint(set(city))
            ]

            for city in found_cities:
                if city not in checked:
                    not_checked.add(city)

        count_networks += 1

    count_network_cities = len(checked)
    count_non_network_cities = n - count_network_cities
    cost_roads = c_road * (count_network_cities - count_networks)
    cost_libraries = c_lib * (count_non_network_cities + count_networks)

    return cost_roads + cost_libraries


if __name__ == '__main__':
    # q = PROBLEM_INPUT
    q = process_input('input02.txt')

    # print(q)

    for q_itr in q:
        n = int(q_itr[0])
        c_lib = int(q_itr[1])
        c_road = int(q_itr[2])
        cities = q_itr[3]
        result = roadsAndLibraries(n, c_lib, c_road, cities)
        print(f'result = {result}')
