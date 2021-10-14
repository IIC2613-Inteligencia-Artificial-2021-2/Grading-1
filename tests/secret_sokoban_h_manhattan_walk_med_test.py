from search.problems.grid.sokoban import (SokobanMetaProblem,
                                          SokobanSimpleManhattanActionDistance)
from search.space import Problem

INFINITY = float("inf")


def test_manhattan_walk_multiple_boxes():
    metaproblem = SokobanMetaProblem(
        [
            # This is impossible, but it should look like it needs 3+1 actions.
            "S GB",
            "  GB",
            "  GB",
        ]
    )
    problem: Problem = next(iter(metaproblem.multi_goal_given()))
    start = next(iter(problem.starting_states))

    # pylint: disable=invalid-name
    h = SokobanSimpleManhattanActionDistance(problem)
    assert h(start) == 4


def test_manhattan_walk_multiple_boxes_2():
    metaproblem = SokobanMetaProblem(
        [
            # This is impossible, but it should look like it needs 2+1 actions.
            "S BGB",
            "     ",
            "G    ",
        ]
    )
    problem: Problem = next(iter(metaproblem.multi_goal_given()))
    start = next(iter(problem.starting_states))

    # pylint: disable=invalid-name
    h = SokobanSimpleManhattanActionDistance(problem)
    assert h(start) == 3


def test_manhattan_walk_multiple_boxes_3():
    metaproblem = SokobanMetaProblem(
        [
            # This looks like it needs 2+3 actions.
            "S   BG ",
            "     B ",
            "       ",
            "G      ",
        ]
    )
    problem: Problem = next(iter(metaproblem.multi_goal_given()))
    start = next(iter(problem.starting_states))

    # pylint: disable=invalid-name
    h = SokobanSimpleManhattanActionDistance(problem)
    assert h(start) == 5
