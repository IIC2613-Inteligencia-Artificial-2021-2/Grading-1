"""
Tests for A* Search algorithm.
"""

from typing import Optional

from search.algorithms.astar import AStar
from search.algorithms.search import Node, SearchAlgorithm
from search.problems.grid.board2d import (
    Grid2D,
    Grid2DManhattanDistance,
    Grid2DMetaProblem,
)
from search.space import Problem


def test_f_same_g():
    state = Grid2D.State((0, 0))

    # pylint: disable=invalid-name
    node_1 = AStar.AStarNode(state, action=None, parent=None, g=10, h=1)
    node_2 = AStar.AStarNode(state, action=None, parent=None, g=10, h=2)

    assert node_1 < node_2


def test_f_same_h():
    state = Grid2D.State((0, 0))

    # pylint: disable=invalid-name
    node_1 = AStar.AStarNode(state, action=None, parent=None, g=10, h=1)
    node_2 = AStar.AStarNode(state, action=None, parent=None, g=11, h=1)

    assert node_1 < node_2
