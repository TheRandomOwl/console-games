from c4 import Grid

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
    state = board.check_winner()
    if state:
        return 1 if state == symbol else -1
    elif board.is_full():
        return 0
    elif depth == 0:
        return 0
    
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
            board.add_move(move, 'X' if symbol == 'O' else 'O')
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
        score = minimax(board, symbol, False, 8, -float('inf'), float('inf'))
        board.grid = old
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def main():
    board = Grid()
    print(board)
    while board.check_winner() == None and not board.is_full():
        col = int(input("Enter column: "))
        board.add_move(col, 'X')
        print(board)
        col = best_move(board, 'O')
        board.add_move(col, 'O')
        print(board)
    if board.check_winner() == 'X':
        print("You win!")
    elif board.check_winner() == 'O':
        print("You lose!")
    else:
        print("It's a draw!")
        
if __name__ == "__main__":
    main()
    