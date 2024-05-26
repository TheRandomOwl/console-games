def minimax(board, symbol, maximizing):
    """
    Minimax algorithm for tic-tac-toe.

    Parameters:
    - board: The current state of the tic-tac-toe board.
    - symbol: The symbol ('X' or 'O') of the player making the move.
    - maximizing: A boolean value to indicate if the player is maximizing or minimizing.

    Returns:
    - The best score for the given board and player.
    """
    state = board.check_winner()
    if state:
        return 1 if state == symbol else -1
    elif board.is_full():
        return 0
    
    if maximizing:
        value = -float('inf')
        for move in board.empty_cells():
            board.add_move(move[0], move[1], symbol)
            value = max(value, minimax(board, symbol, False))
            board.add_move(move[0], move[1], ' ')
        return value
    else:
        value = float('inf')
        for move in board.empty_cells():
            board.add_move(move[0], move[1], 'X' if symbol == 'O' else 'O')
            value = min(value, minimax(board, symbol, True))
            board.add_move(move[0], move[1], ' ')
        return value
    
def best_move(board, symbol):
    """
    Find the best move for the given player using minimax algorithm.

    Parameters:
    - board: The current state of the tic-tac-toe board.
    - symbol: The symbol ('X' or 'O') of the player making the move.

    Returns:
    - The best move for the given player.
    """
    best_score = -float('inf')
    best_move = None
    for move in board.empty_cells():
        board.add_move(move[0], move[1], symbol)
        score = minimax(board, symbol, False)
        board.add_move(move[0], move[1], ' ')
        if score > best_score:
            best_score = score
            best_move = move
    return best_move