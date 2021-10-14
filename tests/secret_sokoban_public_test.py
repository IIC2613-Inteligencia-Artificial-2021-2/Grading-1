from search.problems.grid.sokoban import SokobanMetaProblem
from search.space import Problem

INFINITY = float("inf")


def test_heuristic_no_goal():
    metaproblem = SokobanMetaProblem(
        [
            "S  ",
        ]
    )
    problem: Problem = next(iter(metaproblem.multi_goal_given()))
    start = next(iter(problem.starting_states))

    # pylint: protected-access
    assert problem._eval_heuristics(start) == {
        "SokobanBetterDistance": INFINITY,
        "SokobanSimpleManhattanActionDistance": INFINITY,
        "SokobanSimpleManhattanDistance": INFINITY,
        "SokobanMisplacedBoxes": INFINITY,
        "SokobanDiscreteMetric": 0,
        "Heuristic": 0,
    }


def test_heuristic_single_goal():
    metaproblem = SokobanMetaProblem(
        [
            "S G",
        ]
    )
    problem: Problem = next(iter(metaproblem.multi_goal_given()))
    start = next(iter(problem.starting_states))

    # pylint: protected-access
    assert problem._eval_heuristics(start) == {
        "SokobanBetterDistance": 0,
        "SokobanSimpleManhattanActionDistance": 0,
        "SokobanSimpleManhattanDistance": 0,
        "SokobanMisplacedBoxes": 0,
        "SokobanDiscreteMetric": 0,
        "Heuristic": 0,
    }


def test_heuristic_multi_goal():
    metaproblems = [
        SokobanMetaProblem(
            [
                "                 G",
                " S                ",
                "G                 ",
            ]
        ),
        SokobanMetaProblem(
            [
                "                 G",
                "                S ",
                "G                 ",
            ]
        ),
    ]

    for metaproblem in metaproblems:
        for problem in metaproblem.multi_goal_given():
            start = next(iter(problem.starting_states))
            # pylint: protected-access
            assert problem._eval_heuristics(start) == {
                "SokobanBetterDistance": 0,
                "SokobanSimpleManhattanActionDistance": 0,
                "SokobanSimpleManhattanDistance": 0,
                "SokobanMisplacedBoxes": 0,
                "SokobanDiscreteMetric": 0,
                "Heuristic": 0,
            }
