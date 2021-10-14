"""
Tests for A* Search algorithm.
"""
from search.algorithms.astar import AStar
from search.problems.grid.board2d import Grid2D


def test_tie_breaking():
    state = Grid2D.State((0, 0))

    # pylint: disable=invalid-name
    f = 5
    g1 = 3
    h1 = f - g1
    node_1 = AStar.AStarNode(state, action=None, parent=None, g=g1, h=h1)
    g2 = 2
    h2 = f - g2
    node_2 = AStar.AStarNode(state, action=None, parent=None, g=g2, h=h2)

    assert node_1 < node_2


def test_tie_breaking():
    state = Grid2D.State((0, 0))

    # pylint: disable=invalid-name
    f = 5
    for g1 in range(f+1):
        h1 = f - g1
        node_1 = AStar.AStarNode(state, action=None, parent=None, g=g1, h=h1)
        for g2 in range(f+1):
            h2 = f - g2
            node_2 = AStar.AStarNode(state, action=None, parent=None, g=g2, h=h2)

            if h1 < h2:
                assert node_1 < node_2
            elif h1 > h2:
                assert node_1 > node_2
