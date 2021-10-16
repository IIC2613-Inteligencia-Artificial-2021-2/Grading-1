from search.problems.grid.sokoban import (
    SokobanMetaProblem,
    SokobanSimpleManhattanActionDistance,
)
from search.space import Problem


def test_manhattan_walk_goal_state():
    metaproblem = SokobanMetaProblem(
        [
            # Technically every box is in a goal.
            "S G",
        ]
    )
    problem: Problem = next(iter(metaproblem.multi_goal_given()))
    start = next(iter(problem.starting_states))

    # pylint: disable=invalid-name
    h = SokobanSimpleManhattanActionDistance(problem)
    assert h(start) == 0


def test_manhattan_walk_single_box():
    metaproblem = SokobanMetaProblem(
        [
            # This is impossible, but it should look like it needs 1+1 action.
            "S BG",
        ]
    )
    problem: Problem = next(iter(metaproblem.multi_goal_given()))
    start = next(iter(problem.starting_states))

    # pylint: disable=invalid-name
    h = SokobanSimpleManhattanActionDistance(problem)
    assert h(start) == 2
