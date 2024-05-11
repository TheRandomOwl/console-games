class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.points = 0

def tic_tac_toe(players):
  import tic.ttt as ttt
  board = ttt.Grid()
  clear_console()
  print(board)
  
  def replay():
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == "y":
      board.clear()
      clear_console()
      print(board)
      return True
    else:
      return False

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
            print(f"Score: {players[0].name}: {players[0].points}, {players[1].name}: {players[1].points}")
            if not replay():
              return
          elif board.is_full():
            print("It's a tie!")
            if not replay():
              return
          break
        else:
          print("Invalid move, try again")

def connect_four(players):
  print("Connect Four")

def clear_console():
    import os
    os.system("cls" if os.name == "nt" else "clear")
    
def exit_game():
  clear_console()
  print("Goodbye!")
  exit()

def main():
  p1 = Player("Player 1", "X")
  p2 = Player("Player 2", "O")

  options = {
    "1": {"name": "Tic Tac Toe", "function": tic_tac_toe},
    "2": {"name": "Connect Four", "function": connect_four},
    "3": {"name": "Exit", "function": exit_game}
  }

  clear_console()
  print("Welcome to console games! Select a game to play")
  while True:
    for i, option in options.items():
      print(f"{i}. {option['name']}")
      
    choice = input("Enter the number of the game you want to play: ")
    if choice in options:
      selected_option = options[choice]
      if selected_option["name"] != "Exit":
        selected_option["function"]([p1, p2])
      else:
        # dont pass players to exit function
        selected_option["function"]()
    else:
      print("Invalid choice")

if __name__ == "__main__":
    main()
