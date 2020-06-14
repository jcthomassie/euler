# -*- coding: utf-8 -*-
"""
Path sum: two ways
==================
https://projecteuler.net/problem=81

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom
right, by only moving to the right and down, is indicated in bold red and is
equal to 2427.

        [131]  673   234   103    18

        [201] [ 96] [342]  965   150

         630   803  [746] [422]  111

         537   699   497  [121]  956

         805   732   524  [ 37] [331]

Find the minimal path sum from the top left to the bottom right by only moving
right and down in matrix.txt, a 31K text file containing an 80 by 80 matrix.
"""
import math
import os
from collections import defaultdict

import numpy as np

from . import DATA_DIR
from .utils import print_result

TEST = np.array([
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37, 331],
])

def scrape_array(path: str):
    """
    Scrape array from text file.
    """
    with open(path, "r") as h:
        matrix = []
        for line in h:
            matrix.append([
                int(node) for node in line.strip().split(",")
            ])
    return np.array(matrix)

def a_star(
        array,
        start=None,
        end=None,
        neighbors=None,
    ):
    """
    Find the optimal path sum through the input array of node weights using the
    A* algorithm.
    """
    if start is None:
        start = (0, 0)
    if end is None:
        end = (array.shape[0] - 1, array.shape[1] - 1)
    if neighbors is None:
        neighbors = ((1, 0), (0, 1), (-1, 0), (0, -1))

    def heuristic(n):
        return array.min() * (sum(abs(b - a) for a, b in zip(n, end)) - 1)

    candidates = set([start])
    parents = dict()
    # Best known scores
    g_scores = defaultdict(lambda: math.inf)
    g_scores[start] = array[start[0], start[1]]
    # Estimated optimal scores
    f_scores = defaultdict(lambda: math.inf)
    f_scores[start] = heuristic(start)
    while candidates:
        node = min(candidates, key=lambda n: f_scores[n])
        # Return path if reached end
        if node == end:
            path = [array[node[0], node[1]]]
            while node in parents:
                node = parents[node]
                path.append(array[node[0], node[1]])
            return path[::-1]
        candidates.remove(node)

        # Check all neighbors to see if current node is better entry point
        for di, dj in neighbors:
            ni = node[0] + di
            nj = node[1] + dj
            neighbor = (ni, nj)
            if not 0 <= ni < array.shape[0] or not 0 <= nj < array.shape[1]:
                continue
            # See if score to neighbor is best
            score = g_scores[node] + array[node[0], node[1]]
            if score < g_scores[neighbor]:
                parents[neighbor] = node
                g_scores[neighbor] = score
                f_scores[neighbor] = score + heuristic(neighbor)
                candidates.add(neighbor)

@print_result
def solve():
    return sum(a_star(
        scrape_array(os.path.join(DATA_DIR, "p081_matrix.txt")),
        neighbors=((0, 1), (1, 0)),
    ))

if __name__ == "__main__":
    solve()
