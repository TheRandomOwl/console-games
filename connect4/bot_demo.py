from bot import best_move
from c4 import Grid

def bot_demo():
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
    bot_demo()