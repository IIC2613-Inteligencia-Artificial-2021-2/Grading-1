"""
Tests for the Breadth-first Search algorithm.
"""

from typing import Optional

from search.algorithms.iddfs import IDDFS
from search.algorithms.search import Node, SearchAlgorithm
from search.problems.grid.board2d import Grid2DMetaProblem
from search.space import Problem


def test_no_solution():
    metaproblem = Grid2DMetaProblem(
        [
            "     ",
            "#### ",
            "     ",
            "S    ",
        ]
    )
    problem: Problem = next(iter(metaproblem.multi_goal_given()))
    depth_limit = 18
    iddfs: SearchAlgorithm = IDDFS(problem, depth_limit)
    iddfs.expansion_limit = 20_000

    # Search
    goal_node: Optional[Node] = iddfs.search()

    # A solution must not be found
    assert goal_node is None

    # This maps needs to be completely expanded
    # Without loop detection this may run forever
    assert iddfs.expansions > 66
