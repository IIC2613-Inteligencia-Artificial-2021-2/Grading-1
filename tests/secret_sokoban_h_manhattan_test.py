from search.problems.grid.sokoban import (
    SokobanMetaProblem,
    SokobanSimpleManhattanDistance,
)
from search.space import Problem

INFINITY = float("inf")


def test_manhattan_goal_state():
    metaproblem = SokobanMetaProblem(
        [
            # Technically every box is in a goal.
            "S G",
        ]
    )
    problem: Problem = next(iter(metaproblem.multi_goal_given()))
    start = next(iter(problem.starting_states))

    # pylint: disable=invalid-name
    h = SokobanSimpleManhattanDistance(problem)
    assert h(start) == 0


def test_manhattan_single_box():
    metaproblem = SokobanMetaProblem(
        [
            # This is impossible, but it should look like it needs 1 action.
            "S BG",
        ]
    )
    problem: Problem = next(iter(metaproblem.multi_goal_given()))
    start = next(iter(problem.starting_states))

    # pylint: disable=invalid-name
    h = SokobanSimpleManhattanDistance(problem)
    assert h(start) == 1


def test_manhattan_multiple_boxes():
    metaproblem = SokobanMetaProblem(
        [
            # This is impossible, but it should look like it needs 3 actions.
            "S GB",
            "  GB",
            "  GB",
        ]
    )
    problem: Problem = next(iter(metaproblem.multi_goal_given()))
    start = next(iter(problem.starting_states))

    # pylint: disable=invalid-name
    h = SokobanSimpleManhattanDistance(problem)
    assert h(start) == 3


def test_manhattan_multiple_boxes_2():
    metaproblem = SokobanMetaProblem(
        [
            # This is impossible, but it should look like it needs 2 actions.
            "S BGB",
            "     ",
            "G    ",
        ]
    )
    problem: Problem = next(iter(metaproblem.multi_goal_given()))
    start = next(iter(problem.starting_states))

    # pylint: disable=invalid-name
    h = SokobanSimpleManhattanDistance(problem)
    assert h(start) == 2


def test_manhattan_multiple_boxes_3():
    metaproblem = SokobanMetaProblem(
        [
            # This looks like it needs 2 actions.
            "S   BG ",
            "     B ",
            "       ",
            "G      ",
        ]
    )
    problem: Problem = next(iter(metaproblem.multi_goal_given()))
    start = next(iter(problem.starting_states))

    # pylint: disable=invalid-name
    h = SokobanSimpleManhattanDistance(problem)
    assert h(start) == 2
