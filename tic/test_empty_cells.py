from ttt import Grid

def test_empty_cells():
    """
    Test case for getting the empty cells in the grid.
    """
    grid = Grid()
    assert grid.empty_cells() == [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

    grid.add_move(0, 0, 'X')
    grid.add_move(1, 1, 'O')
    assert grid.empty_cells() == [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]

    grid.add_move(2, 2, 'X')
    assert grid.empty_cells() == [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]

    grid.clear()
    assert grid.empty_cells() == [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]