# -*- coding: utf-8 -*-
"""
Triangle containment
====================
https://projecteuler.net/problem=102

Three distinct points are plotted at random on a Cartesian plane, for which
-1000 ≤ x, y ≤ 1000, such that a triangle is formed.

Consider the following two triangles:

    A(-340,495), B(-153,-910), C(835,-947)

    X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ
does not.

Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file
containing the co-ordinates of one thousand "random" triangles, find the number
of triangles for which the interior contains the origin.

NOTE: The first two examples in the file represent the triangles in the example
given above.
"""
from itertools import combinations
from typing import Iterator, Tuple

from . import DATA_DIR
from .utils import print_result

Point = Tuple[int, int]
Triangle = Tuple[Point, Point, Point]


def positive_x_intercept(point_a: Point, point_b: Point) -> bool:
    """Return True if a line drawn between the input points has a positive
    X-intercept."""
    x_a, y_a = point_a
    x_b, y_b = point_b
    # Does not cross X = 0
    if (x_a < 0) and (x_b < 0):
        return False
    # Does not cross Y = 0
    if (y_a > 0) == (y_b > 0):
        return False
    # Check if intercept is positive
    return x_b > y_b * (x_b - x_a) / (y_b - y_a)


def contains_origin(triangle: Triangle) -> bool:
    """Return True if the input triangle contains the origin (0, 0).

    Strategy comes from the ray casting algorithm:
    https://en.wikipedia.org/wiki/Point_in_polygon#Ray_casting_algorithm

    If the triangle contains the origin, exactly one edge will have a positive
    y-intercept.
    """
    return sum(positive_x_intercept(*edge) for edge in combinations(triangle, 2)) == 1


def scrape_triangles() -> Iterator[Triangle]:
    with open(DATA_DIR / "p102_triangles.txt", "r") as f:
        for line in f:
            coords = tuple(int(n) for n in line.split(","))
            yield (coords[:2], coords[2:4], coords[4:6])  # type: ignore


@print_result
def solve() -> int:
    return sum(contains_origin(triangle) for triangle in scrape_triangles())


if __name__ == "__main__":
    solve()
