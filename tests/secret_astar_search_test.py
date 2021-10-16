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


def test_clear_search():
    metaproblem = Grid2DMetaProblem(
        [
            # 12345678901234-
            "                ",
            " S             G",
            "                ",
        ]
    )
    problem: Problem = next(iter(metaproblem.multi_goal_given()))
    heuristic = Grid2DManhattanDistance(problem)
    astar: SearchAlgorithm = AStar(problem, heuristic)

    # Search
    goal_node: Optional[Node] = astar.search()

    # A solution must be found
    assert goal_node is not None
    # This maps needs to be completely expanded
    assert astar.expansions == 14


def test_clear_search_2():
    metaproblem = Grid2DMetaProblem(
        [
            "                 ",
            " S               ",
            "        #        ",
            "               G ",
            "                 ",
        ]
    )
    problem: Problem = next(iter(metaproblem.multi_goal_given()))
    heuristic = Grid2DManhattanDistance(problem)
    astar: SearchAlgorithm = AStar(problem, heuristic)

    # Search
    goal_node: Optional[Node] = astar.search()

    # A solution must be found
    assert goal_node is not None
    # The inner rectangle needs to be expanded completely
    assert astar.expansions <= 43
