from ttt import Grid

def test_no_winner():
    """
    Test case for no winner scenario.
    Board layout:
    X | O | X
    O | X | O
    O | X | O
    """
    grid = Grid()
    grid.add_move(0, 0, 'X')
    grid.add_move(0, 1, 'O')
    grid.add_move(0, 2, 'X')
    grid.add_move(1, 0, 'O')
    grid.add_move(1, 1, 'X')
    grid.add_move(1, 2, 'O')
    grid.add_move(2, 0, 'O')
    grid.add_move(2, 1, 'X')
    grid.add_move(2, 2, 'O')
    assert grid.check_winner() == None

def test_horizontal_win():
    """
    Test case for horizontal win scenario.
    Board layout:
    X | X | X
    """
    grid = Grid()
    grid.add_move(0, 0, 'X')
    grid.add_move(0, 1, 'X')
    grid.add_move(0, 2, 'X')
    assert grid.check_winner() == 'X'

def test_vertical_win():
    """
    Test case for vertical win scenario.
    Board layout:
    O |   |
    O |   |
    O |   |
    """
    grid = Grid()
    grid.add_move(0, 0, 'O')
    grid.add_move(1, 0, 'O')
    grid.add_move(2, 0, 'O')
    assert grid.check_winner() == 'O'

def test_diagonal_win():
    """
    Test case for diagonal win scenario.
    Board layout:
    X |   |
      | X |
      |   | X
    """
    grid = Grid()
    grid.add_move(0, 0, 'X')
    grid.add_move(1, 1, 'X')
    grid.add_move(2, 2, 'X')
    assert grid.check_winner() == 'X'

def test_reverse_diagonal_win():
    """
    Test case for reverse diagonal win scenario.
    Board layout:
      |   | O
      | O |
    O |   |
    """
    grid = Grid()
    grid.add_move(0, 2, 'O')
    grid.add_move(1, 1, 'O')
    grid.add_move(2, 0, 'O')
    assert grid.check_winner() == 'O'
