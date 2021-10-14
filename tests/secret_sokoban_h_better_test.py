from search.problems.grid.sokoban import (Sokoban, SokobanBetterDistance,
                                          SokobanMetaProblem, SokobanProblem,
                                          SokobanSimpleManhattanActionDistance,
                                          SokobanSimpleManhattanDistance)
from search.space import Problem

INFINITY = float("inf")

HEURISTIC_CTORS = [
            SokobanBetterDistance,
            SokobanSimpleManhattanActionDistance,
            SokobanSimpleManhattanDistance,
]


def heuristics(problem: SokobanProblem, state: Sokoban.State):
    """Returns a map from heuristic name to its value for a given instance."""
    return {hc.__name__: hc(problem)(state) for hc in HEURISTIC_CTORS}



def test_heuristic_no_goal():
    metaproblem = SokobanMetaProblem(
        [
            "S  ",
        ]
    )
    problem: Problem = next(iter(metaproblem.multi_goal_given()))
    start = next(iter(problem.starting_states))

    values = heuristics(problem, start)
    assert values["SokobanBetterDistance"] in [0, INFINITY]
    assert values["SokobanSimpleManhattanActionDistance"] == INFINITY
    assert values["SokobanSimpleManhattanDistance"] == INFINITY


def test_heuristic_single_goal():
    metaproblem = SokobanMetaProblem(
        [
            "S G",
        ]
    )
    problem: Problem = next(iter(metaproblem.multi_goal_given()))
    start = next(iter(problem.starting_states))

    values = heuristics(problem, start)
    assert values["SokobanBetterDistance"] in [0, INFINITY]
    assert values["SokobanSimpleManhattanActionDistance"] == 0
    assert values["SokobanSimpleManhattanDistance"] == 0


def test_heuristic_impossible():
    metaproblem = SokobanMetaProblem(
        [
            "SGB",
        ]
    )
    problem: Problem = next(iter(metaproblem.multi_goal_given()))
    start = next(iter(problem.starting_states))

    values = heuristics(problem, start)
    assert values["SokobanBetterDistance"] >= 1
    if values["SokobanSimpleManhattanActionDistance"] != 1:
        print("The value for SokobanSimpleManhattanActionDistance should be 1")
        print(str(start))
        print(values)
    if values["SokobanSimpleManhattanDistance"] != 1:
        print("The value for SokobanSimpleManhattanDistance should be 1")
        print(str(start))
        print(values)


def test_heuristic_parallel():
    metaproblem = SokobanMetaProblem(
        [
            "   # GB",
            "S  # GB",
            "   # GB",
        ]
    )
    problem: Problem = next(iter(metaproblem.multi_goal_given()))
    start = next(iter(problem.starting_states))

    values = heuristics(problem, start)
    assert values["SokobanBetterDistance"] >= 8
    if values["SokobanSimpleManhattanActionDistance"] != 8:
        print("The value for SokobanSimpleManhattanActionDistance should be 8")
        print(str(start))
        print(values)
    if values["SokobanSimpleManhattanDistance"] != 3:
        print("The value for SokobanSimpleManhattanDistance should be 3")
        print(str(start))
        print(values)


def test_heuristic_parallel():
    metaproblem = SokobanMetaProblem(
        [
            "   B         G",
            "   B         G",
            "S  BG        G",
            "   B         G",
            "   B         G",
        ]
    )
    problem: Problem = next(iter(metaproblem.multi_goal_given()))
    start = next(iter(problem.starting_states))

    values = heuristics(problem, start)
    assert 13 <= values["SokobanBetterDistance"] <= 80
    if values["SokobanSimpleManhattanActionDistance"] != 13:
        print("The value for SokobanSimpleManhattanActionDistance should be 13")
        print(str(start))
        print(values)
    if values["SokobanSimpleManhattanDistance"] != 11:
        print("The value for SokobanSimpleManhattanDistance should be 11")
        print(str(start))
        print(values)
