from c4 import Grid
import random

def test_clear():
    """
    Test case for clearing the grid.
    """
    grid = Grid()
    grid.grid = [['X' for i in range(7)] for j in range(6)]
    grid.clear()
    assert grid.grid == [[' ' for i in range(7)] for j in range(6)]

def test_add_move():
    """
    Test case for adding a move to the grid.
    """
    grid = Grid()
    
    col = random.randint(0,6)
    grid.add_move(col, 'X')
    assert grid.grid[0][col] == 'X'
    grid.add_move(col, 'O')
    assert grid.grid[1][col] == 'O'
    
    grid.clear()
    col = random.randint(0,6)
    for i in range(0, 6):
        grid.add_move(col, 'X')
        assert grid.grid[i][col] == 'X'

def test_is_valid_move():
    """
    Test case for checking if a move is valid.
    """
    grid = Grid()
    assert grid.is_valid_move(0) == True
    assert grid.is_valid_move(7) == False
    assert grid.is_valid_move(-1) == False

    for i in range(6):
        grid.add_move(0, 'X')
    assert grid.is_valid_move(0) == False

    grid.clear()
    grid.add_move(0, 'X')
    assert grid.is_valid_move(0) == True

def test_is_full():
    """
    Test case for checking if the grid is full.
    """
    grid = Grid()
    assert grid.is_full() == False

    grid.grid = [['X' for i in range(7)] for j in range(6)]
    assert grid.is_full() == True

    grid.clear()
    for i in range(7):
        for j in range(random.randint(0, 5)):
            grid.add_move(i, 'X')
    assert grid.is_full() == False

def test_check_winner():
    """
    Test case for checking if there is a winner.
    """
    grid = Grid()

    # Test horizontal win
    grid.grid = [['X', 'X', 'X', 'X', ' ', ' ', ' '],
                 ['O', 'O', 'O', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    assert grid.check_winner() == 'X'

    # Test vertical win
    grid.grid = [['X', 'O', ' ', ' ', ' ', ' ', ' '],
                 ['X', 'O', ' ', ' ', ' ', ' ', ' '],
                 ['X', 'O', ' ', ' ', ' ', ' ', ' '],
                 ['X', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    assert grid.check_winner() == 'X'

    # Test diagonal win (top-left to bottom-right)
    grid.grid = [['X', 'O', 'O', 'O', ' ', ' ', ' '],
                 ['O', 'X', 'X', 'X', ' ', ' ', ' '],
                 [' ', 'O', 'X', 'O', ' ', ' ', ' '],
                 [' ', ' ', 'X', 'X', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    assert grid.check_winner() == 'X'

    # Test diagonal win (top-right to bottom-left)
    grid.grid = [[' ', ' ', ' ', 'O', 'O', 'O', 'X'],
                 [' ', ' ', ' ', 'X', 'O', 'X', ' '],
                 [' ', ' ', ' ', 'O', 'X', ' ', ' '],
                 [' ', ' ', ' ', 'X', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    assert grid.check_winner() == 'X'

    # Test no winner
    grid.grid = [['O', 'O', 'X', 'X', 'O', 'X', 'X'],
                 ['O', 'O', 'X', 'X', 'O', 'O', 'X'],
                 ['X', 'X', 'O', 'O', 'X', 'X', 'O'],
                 ['O', 'O', 'X', 'X', 'X', 'O', 'X'],
                 ['X', 'X', 'X', 'O', 'X', 'X', 'X'],
                 ['O', 'O', 'O', 'X', 'O', 'O', 'O']]
    assert grid.check_winner() == None

def main():
    test_clear()
    test_add_move()
    test_is_valid_move()
    test_is_full()
    test_check_winner()
    print("All tests passed.")

if __name__ == "__main__":
    main()