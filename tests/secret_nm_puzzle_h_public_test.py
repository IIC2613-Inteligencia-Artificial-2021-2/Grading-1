"""
Tests for the NM-puzzle. A generalization of the 8-puzzle

An implementation detail that could be surprising, is that the empty space uses
the highest number instead of 0.
"""
import numpy as np
from search.problems.nm_puzzle import (NMPuzzleManhattanDistance,
                                       NMPuzzleMetaProblem)


def test_heuristic_single_tile_off():
    metaproblem = NMPuzzleMetaProblem(
        np.array(
            [
                [0, 1],
                [3, 2],
            ]
        )
    )
    problem = next(iter(metaproblem.simple_given()))
    start = next(iter(problem.starting_states))

    # pylint: disable=invalid-name
    h = NMPuzzleManhattanDistance(problem)
    assert h(start) == 1


def test_heuristic_reversed_tiles():
    metaproblem = NMPuzzleMetaProblem(
        np.array(
            [
                [8, 7, 6],
                [5, 4, 3],
                [2, 1, 0],
            ]
        )
    )
    problem = next(iter(metaproblem.simple_given()))
    start = next(iter(problem.starting_states))

    # pylint: disable=invalid-name
    h = NMPuzzleManhattanDistance(problem)
    assert h(start) == 20
