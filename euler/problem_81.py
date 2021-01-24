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
from collections import defaultdict
from pathlib import Path
from typing import Optional

import numpy as np

from . import DATA_DIR
from .utils import print_result

TEST = np.array(
    [
        [131, 673, 234, 103, 18],
        [201, 96, 342, 965, 150],
        [630, 803, 746, 422, 111],
        [537, 699, 497, 121, 956],
        [805, 732, 524, 37, 331],
    ]
)


def scrape_array(path: Path) -> np.array:
    """Scrape array from text file."""
    with path.open() as h:
        matrix = []
        for line in h:
            matrix.append([int(node) for node in line.strip().split(",")])
    return np.array(matrix)


Node = tuple[int, int]


def a_star(
    array: np.array,
    start: Optional[Node] = None,
    end: Optional[Node] = None,
    neighbors: Optional[tuple[Node, ...]] = None,
) -> list[int]:
    """
    Find the optimal path through the input array of node weights using the
    A* algorithm.
    """
    if start is None:
        start = (0, 0)
    if end is None:
        end = (array.shape[0] - 1, array.shape[1] - 1)
    if neighbors is None:
        neighbors = ((1, 0), (0, 1), (-1, 0), (0, -1))

    candidates = set([start])
    parents: dict[Node, Node] = dict()
    # Best known scores
    scores = defaultdict(lambda: math.inf)
    scores[start] = array[start[0], start[1]]
    while candidates:
        node = min(candidates, key=scores.__getitem__)
        # Return path weights if reached end
        if node == end:
            path = [array[node[0], node[1]]]
            while node in parents:
                node = parents[node]
                path.append(array[node[0], node[1]])
            return path[::-1]
        candidates.remove(node)

        # Check all neighbors to see if current node is better entry point
        score = scores[node] + array[node[0], node[1]]
        for di, dj in neighbors:
            ni = node[0] + di
            nj = node[1] + dj
            neighbor = (ni, nj)
            if not 0 <= ni < array.shape[0] or not 0 <= nj < array.shape[1]:
                continue
            # See if score to neighbor is best
            if score < scores[neighbor]:
                parents[neighbor] = node
                scores[neighbor] = score
                candidates.add(neighbor)
    raise RuntimeError("Failed to find path")


@print_result
def solve() -> int:
    return sum(
        a_star(
            scrape_array(DATA_DIR / "p081_matrix.txt"),
            neighbors=((0, 1), (1, 0)),
        )
    )


if __name__ == "__main__":
    solve()
