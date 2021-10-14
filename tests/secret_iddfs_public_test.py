"""
Tests for the Breadth-first Search algorithm.
"""

from typing import Optional

from search.algorithms.iddfs import IDDFS
from search.algorithms.search import Node, SearchAlgorithm
from search.problems.grid.board2d import Grid2DMetaProblem
from search.space import Problem


def test_solution():
    metaproblem = Grid2DMetaProblem(
        [
            "G    ",
            "#### ",
            "     ",
            "S    ",
        ]
    )
    problem: Problem = next(iter(metaproblem.multi_goal_given()))
    iddfs: SearchAlgorithm = IDDFS(problem)
    iddfs.expansion_limit = 25_000

    # Search
    goal_node: Optional[Node] = iddfs.search()

    # A solution must be found
    assert goal_node is not None

    # We can get its path
    path = goal_node.path(problem.space)
    assert path is not None

    # And it should be optimal.
    assert path.cost() == 11

    # The map is more than completely expanded.
    assert 66 < iddfs.expansions


def test_expansion_order():
    length = 30
    metaproblem = Grid2DMetaProblem(
        [
            "G" + " " * length + "S" + " " * length,
        ]
    )
    problem: Problem = next(iter(metaproblem.multi_goal_given()))
    iddfs: SearchAlgorithm = IDDFS(problem)
    iddfs.expansion_limit = 25_000

    # Search
    goal_node: Optional[Node] = iddfs.search()

    assert goal_node is not None
    assert goal_node.path(problem.space) is not None
    # It needs more expansions than BFS
    assert iddfs.expansions > 2 * (length + 1)
