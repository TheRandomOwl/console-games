import ttt
from bot import best_move

def bot_demo():
    board = ttt.Grid()
    print(board)
    while True:
        try:
            row = int(input("Enter row: "))
            col = int(input("Enter column: "))
        except ValueError:
            print("Invalid input, try again")
            continue
        if board.is_valid_move(row, col):
            board.add_move(row, col, 'X')
            print(board)
            if board.check_winner():
                print("You win!")
                break
            if board.is_full():
                print("It's a tie!")
                break
            move = best_move(board, 'O')
            board.add_move(move[0], move[1], 'O')
            print(board)
            if board.check_winner():
                print("You lose!")
                break
            if board.is_full():
                print("It's a tie!")
                break
        else:
            print("Invalid move, try again")

if __name__ == "__main__":
    bot_demo()