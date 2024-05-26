def evaluate_board(board, symbol):
    """
    Evaluation function to assess the board state for the given symbol.
    
    Parameters:
    - board: The current state of the Connect Four board.
    - symbol: The symbol ('X' or 'O') of the player to evaluate for.
    
    Returns:
    - A score representing the board evaluation.
    """
    # Implement a heuristic to evaluate the board
    score = 0
    # Example: +10 for 3 in a row, -10 for opponent's 3 in a row, etc.
    # This is a placeholder and should be replaced with a proper evaluation.
    # Add your evaluation logic here.

    opponent = 'X' if symbol == 'O' else 'O'

    # prioritize center column
    center_col = [row[3] for row in board.grid]
    score += center_col.count(symbol) * 5

    for row in board.grid:
        if ' ' + opponent * 2 + ' ' in ''.join(row):
            score -= 10
        if ' ' + symbol * 2 + ' ' in ''.join(row):
            score += 10
        if ' ' + opponent * 3 + ' ' in ''.join(row):
            score -= 20
        if ' ' + symbol * 3 + ' ' in ''.join(row):
            score += 20
    
    # Check rows
    for row in range(6):
        for col in range(4):
            if board.grid[row][col:col+4].count(symbol) == 3:
                score += 10
            if board.grid[row][col:col+4].count(opponent) == 3:
                score -= 10
    # Check columns
    for col in range(7):
        for row in range(3):
            if [board.grid[row+i][col] for i in range(4)].count(symbol) == 3:
                score += 10
            if [board.grid[row+i][col] for i in range(4)].count(opponent) == 3:
                score -= 10
    # Check diagonals
    for row in range(3):
        for col in range(4):
            if [board.grid[row+i][col+i] for i in range(4)].count(symbol) == 3:
                score += 10
            if [board.grid[row+i][col+i] for i in range(4)].count(opponent) == 3:
                score -= 10
    for row in range(3):
        for col in range(4):
            if [board.grid[row+i][col-i] for i in range(4)].count(symbol) == 3:
                score += 10
            if [board.grid[row+i][col-i] for i in range(4)].count(opponent) == 3:
                score -= 10
    return score

def minimax(board, symbol, maximizing, depth, alpha, beta):
    """
    Minimax algorithm for connect four with alpha beta pruning.

    Parameters:
    - board: The current state of the tic-tac-toe board.
    - symbol: The symbol ('X' or 'O') of the player making the move.
    - maximizing: A boolean value to indicate if the player is maximizing or minimizing.
    - depth: The current depth of the search.
    - alpha: The alpha value for alpha-beta pruning.
    - beta: The beta value for alpha-beta pruning.

    Returns:
    - The best score for the given board and player.
    """

    opponent = 'X' if symbol == 'O' else 'O'

    state = board.check_winner()
    if state:
        return 10 if state == symbol else -10
    elif board.is_full():
        return 0
    elif depth == 0:
        return evaluate_board(board, symbol)
    
    if maximizing:
        value = -float('inf')
        for move in board.free_col():
            old = [row.copy() for row in board.grid]
            board.add_move(move, symbol)
            value = max(value, minimax(board, symbol, False, depth-1, alpha, beta))
            board.grid = old
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float('inf')
        for move in board.free_col():
            old = [row.copy() for row in board.grid]
            board.add_move(move, opponent)
            value = min(value, minimax(board, symbol, True, depth-1, alpha, beta))
            board.grid = old
            beta = min(beta, value)
            if alpha >= beta:
                break
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
    for move in board.free_col():
        old = [row.copy() for row in board.grid]
        board.add_move(move, symbol)
        score = minimax(board, symbol, False, 6, -float('inf'), float('inf'))
        board.grid = old
        if score > best_score:
            best_score = score
            best_move = move
    return best_move