def minimax(board, symbol, maximizing=True, depth=0):
    """
    Minimax algorithm with alpha-beta pruning for tic-tac-toe.

    This function returns the best move for the given board and player.

    Parameters:
    - board: The current state of the tic-tac-toe board.
    - symbol: The symbol ('X' or 'O') of the player making the move.
    - maximizing: A boolean indicating whether the current player is maximizing or not. Default is True.
    - depth: The depth of the current recursive call. Default is 0.

    Returns:
    - The best score for the given board and player.

    """
    if board.check_winner() == 'X':
        return -10 + depth
    elif board.check_winner() == 'O':
        return 10 - depth
    elif board.is_full():
        return 0
    if maximizing:
        best_score = -100
        for cell in board.empty_cells():
            board.add_move(cell[0], cell[1], symbol)
            score = minimax(board, 'O' if symbol == 'X' else 'X', False, depth + 1)
            board.add_move(cell[0], cell[1], ' ')
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = 100
        for cell in board.empty_cells():
            board.add_move(cell[0], cell[1], symbol)
            score = minimax(board, 'O' if symbol == 'X' else 'X', True, depth + 1)
            board.add_move(cell[0], cell[1], ' ')
            best_score = min(score, best_score)
        return best_score

def get_best_move(board, symbol):
    """
    Returns the best move for the given board and player using the minimax algorithm.

    Parameters:
    - board: The current state of the tic-tac-toe board.
    - symbol: The symbol ('X' or 'O') of the player making the move.

    Returns:
    - The best move for the given board and player.

    """
    best_score = -100
    best_move = None
    for cell in board.empty_cells():
        board.add_move(cell[0], cell[1], symbol)
        score = minimax(board, 'O' if symbol == 'X' else 'X', maximizing=False)
        board.add_move(cell[0], cell[1], ' ')
        if score > best_score:
            best_score = score
            best_move = cell
    return best_move

def main():
    from ttt import Grid
    board = Grid()
    while board.check_winner() is None and not board.is_full():
        print(board)
        row, col = get_best_move(board, 'X')
        board.add_move(row, col, 'X')
        if board.check_winner() is not None:
            print(board)
            print("You lose!")
            break
        elif board.is_full():
            print(board)
            print("It's a tie!")
            break
        print(board)
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))
        if board.is_valid_move(row, col):
            board.add_move(row, col, 'O')
        else:
            print("Invalid move, try again")

if __name__ == "__main__":
    main()