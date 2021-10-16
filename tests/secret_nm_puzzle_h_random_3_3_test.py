"""
Tests for the NM-puzzle. A generalization of the 8-puzzle

An implementation detail that could be surprising, is that the empty space uses
the highest number instead of 0.
"""
import copy
import random

import numpy as np
from search.problems.nm_puzzle import (
    NMPuzzle,
    NMPuzzleManhattanDistance,
    NMPuzzleProblem,
)


def build_goal_state(height: int, width: int) -> NMPuzzle.State:
    """Builds the canonical Goal State."""
    goal_grid = np.full((height, width), 0)
    tile = 0
    # pylint: disable=invalid-name
    for y in range(height):
        for x in range(width):
            goal_grid[y][x] = tile
            tile += 1

    return NMPuzzle.State(goal_grid)


def test_heuristic_random_bound():
    """Create a small instance and ask for"""
    attempts = 30
    max_steps = 10
    for attempt in range(attempts):
        random.seed(attempt)

        goal_state = build_goal_state(height=3, width=3)
        starting_state = copy.deepcopy(goal_state)
        space = NMPuzzle(starting_state.grid)

        state = copy.deepcopy(goal_state)
        for steps in range(max_steps):
            problem = NMPuzzleProblem(
                space, set([copy.deepcopy(state)]), set([goal_state])
            )
            h = NMPuzzleManhattanDistance(problem)

            start = next(iter(problem.starting_states))
            # pylint: disable=invalid-name
            print(str(start))
            assert h(start) <= steps, "This problem can be solved in %d steps: %s" % (
                steps,
                str(start),
            )
            if start != goal_state:
                assert h(start) > 0, "This problem requires some steps: %s" % str(start)

            (_, state) = random.choice(list(space.neighbors(state)))
