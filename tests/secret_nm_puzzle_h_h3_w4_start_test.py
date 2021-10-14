"""
Tests for the NM-puzzle. A generalization of the 8-puzzle

An implementation detail that could be surprising, is that the empty space uses
the highest number instead of 0.
"""
import numpy as np
from search.problems.nm_puzzle import (NMPuzzleManhattanDistance,
                                       NMPuzzleMetaProblem)


def test_heuristic_start():
    metaproblem = NMPuzzleMetaProblem(
        np.array(
            [
                [0, 1,  2,  3],
                [4, 5,  6,  7],
                [8, 9, 10, 11],
            ]
        )
    )
    problem = next(iter(metaproblem.simple_given()))
    start = next(iter(problem.starting_states))

    # pylint: disable=invalid-name
    h = NMPuzzleManhattanDistance(problem)
    assert h(start) == 0


def test_heuristic_reverse():
    metaproblem = NMPuzzleMetaProblem(
        np.array(
            [
                [11, 10, 9, 8],
                [ 7,  6, 5, 4],
                [ 3,  2, 1, 0],
            ]
        )
    )
    problem = next(iter(metaproblem.simple_given()))
    start = next(iter(problem.starting_states))

    # pylint: disable=invalid-name
    h = NMPuzzleManhattanDistance(problem)
    assert h(start) == 35
