# -*- coding: utf-8 -*-
"""
Path sum: three ways
====================
https://projecteuler.net/problem=82

NOTE: This problem is a more challenging version of Problem 81.

The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the
left column and finishing in any cell in the right column, and only moving up,
down, and right, is indicated in red and bold; the sum is equal to 994.

         131   673  [234] [103] [ 18]

        [201] [ 96] [342]  965   150

         630   803   746   422   111

         537   699   497   121   956

         805   732   524    37   331

Find the minimal path sum from the left column to the right column in matrix.txt
(right click and "Save Link/Target As..."), a 31K text file containing an 80 by
80 matrix.
"""
import math
from collections import defaultdict

import numpy as np

from . import DATA_DIR
from .problem_81 import Node, scrape_array
from .utils import print_result


def modified_a_star(array: np.ndarray) -> list[int]:
    """
    Find the optimal path sum through the input array of node weights using the
    A* algorithm. Modified so that any node on left column can be the start
    and any node on the right column can be the end.
    """
    # Special start/end nodes
    start = (-1, -1)
    deltas = ((1, 0), (0, 1), (-1, 0))
    candidates = set([start])
    parents: dict[Node, Node] = dict()
    # Best known scores
    scores: defaultdict[Node, float] = defaultdict(lambda: math.inf)
    scores[start] = 0
    while candidates:
        node = min(candidates, key=lambda n: scores[n])
        # Return path weights if reached end
        if node[1] == array.shape[1] - 1:
            path = [array[node[0], node[1]]]
            while node in parents:
                node = parents[node]
                if node != start:
                    path.append(array[node[0], node[1]])
            return path[::-1]
        candidates.remove(node)

        # Check all neighbors to see if current node is better entry point
        if node == start:
            score = 0
            neighbors = list(((i, 0) for i in range(array.shape[0])))
        else:
            score = scores[node] + array[node[0], node[1]]
            neighbors = []
            for di, dj in deltas:
                ni = node[0] + di
                nj = node[1] + dj
                neighbor = (ni, nj)
                if not 0 <= ni < array.shape[0] or not 0 <= nj < array.shape[1]:
                    continue
                neighbors.append(neighbor)

        for neighbor in neighbors:
            # See if score to neighbor is best
            if score < scores[neighbor]:
                parents[neighbor] = node
                scores[neighbor] = score
                candidates.add(neighbor)
    raise RuntimeError("Failed to find path")


@print_result
def solve() -> int:
    return sum(modified_a_star(scrape_array(DATA_DIR / "p082_matrix.txt")))


if __name__ == "__main__":
    solve()
