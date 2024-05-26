import os
from tic import ttt
from tic import bot
from connect4 import c4

class Player:
  def __init__(self, name, symbol, is_cpu=False):
    self.name = name
    self.symbol = symbol
    self.points = 0
    self.cpu = False

def replay(b):
    play_again = input("Do you want to play again? (y/n): ")
    clear_console()
    if play_again.lower() == "y":
      b.clear()
      print(b)
      return True
    else:
      return False

def tic_tac_toe(players):
  board = ttt.Grid()
  clear_console()
  print(board)

  while True:
    for player in players:
      print(f"{player.name}'s turn")
      while True:
        try:
          row = int(input("Enter row: "))
          col = int(input("Enter column: "))
        except ValueError:
          print("Invalid input, try again")
          continue
        except EOFError:
          clear_console()
          return
        if board.is_valid_move(row, col):
          board.add_move(row, col, player.symbol)
          clear_console()
          print(board)
          winner = board.check_winner()
          if winner:
            print(f"{player.name} wins!")
            player.points += 1
            print_score(players)
            if not replay(board):
              return
          elif board.is_full():
            print("It's a tie!")
            if not replay(board):
              return
          break
        else:
          print("Invalid move, try again")

def connect_four(players):
  board = c4.Grid()
  clear_console()
  print(board)
  while True:
    for player in players:
      print(f"{player.name}'s turn")
      while True:
        try:
          col = int(input("Enter column: "))
        except ValueError:
          print("Invalid input, try again")
          continue
        except EOFError:
          clear_console()
          return
        if board.is_valid_move(col):
          board.add_move(col, player.symbol)
          clear_console()
          print(board)
          winner = board.check_winner()
          if winner:
            print(f"{player.name} wins!")
            player.points += 1
            print_score(players)
            if not replay(board):
              return
          elif board.is_full():
            print("It's a tie!")
            if not replay(board):
              return
          break
        else:
          print("Invalid move, try again")

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")
    
def exit_game():
  clear_console()
  print("Goodbye!")
  exit()

def print_score(players):
  print(f"Score: {players[0].name}: {players[0].points}, {players[1].name}: {players[1].points}")

def main():
  p1 = Player("Player 1", "X")
  p2 = Player("Player 2", "O", True)
  p2.cpu = True
  players = [p1, p2]

  options = {
    "1": {"name": "Tic Tac Toe", "function": tic_tac_toe},
    "2": {"name": "Connect Four", "function": connect_four},
    "3": {"name": "Exit", "function": exit_game}
  }

  clear_console()
  print("Welcome to console games! Select a game to play")
  while True:
    print_score(players)
    for i, option in options.items():
      print(f"{i}. {option['name']}")
    
    try:
      choice = input("Enter the number of the game you want to play: ")
    except KeyboardInterrupt:
      exit_game()
    
    if choice in options:
      selected_option = options[choice]
      if selected_option["name"] != "Exit":
        selected_option["function"](players)
      else:
        # dont pass players to exit function
        selected_option["function"]()
    else:
      print("Invalid choice")

if __name__ == "__main__":
    main()
