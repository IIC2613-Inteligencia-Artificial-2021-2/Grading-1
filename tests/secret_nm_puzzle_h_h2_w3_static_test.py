"""
Tests for the NM-puzzle. A generalization of the 8-puzzle

An implementation detail that could be surprising, is that the empty space uses
the highest number instead of 0.
"""
import numpy as np
from search.problems.nm_puzzle import NMPuzzleManhattanDistance, NMPuzzleMetaProblem


def test_heuristic_1():
    metaproblem = NMPuzzleMetaProblem(
        np.array(
            [
                [4, 3, 0],
                [2, 1, 5],
            ]
        )
    )
    problem = next(iter(metaproblem.simple_given()))
    start = next(iter(problem.starting_states))

    # pylint: disable=invalid-name
    h = NMPuzzleManhattanDistance(problem)
    assert h(start) == 10


def test_heuristic_2():
    metaproblem = NMPuzzleMetaProblem(
        np.array(
            [
                [1, 2, 0],
                [3, 4, 5],
            ]
        )
    )
    problem = next(iter(metaproblem.simple_given()))
    start = next(iter(problem.starting_states))

    # pylint: disable=invalid-name
    h = NMPuzzleManhattanDistance(problem)
    assert h(start) == 4
