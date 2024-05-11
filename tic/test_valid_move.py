from ttt import Grid

def test_valid_move():
    """
    Test case for a valid move.
    """
    grid = Grid()
    assert grid.is_valid_move(0, 0) == True

def test_invalid_move_out_of_bounds():
    """
    Test case for an invalid move that is out of bounds.
    """
    grid = Grid()
    assert grid.is_valid_move(-1, 0) == False
    assert grid.is_valid_move(3, 2) == False

def test_invalid_move_occupied_cell():
    """
    Test case for an invalid move that is on an occupied cell.
    """
    grid = Grid()
    grid.add_move(0, 0, 'X')
    assert grid.is_valid_move(0, 0) == False

def test_invalid_move():
    """
    Test case for an invalid move that is both out of bounds and on an occupied cell.
    """
    grid = Grid()
    grid.add_move(0, 0, 'X')
    assert grid.is_valid_move(-1, 0) == False
    assert grid.is_valid_move(0, 0) == False