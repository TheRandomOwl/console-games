class Grid:
    # create a grid for tic-tac-toe
    def __init__(self):
        self.grid = [[' ' for i in range(3)] for j in range(3)]
    
    # method to add a move to the grid
    def add_move(self, row, col, player):
        self.grid[row][col] = player

    def is_full(self):
        for row in self.grid:
            for cell in row:
                if cell == ' ':
                    return False
        return True
    
    def check_winner(self):
        for i in range(3):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] and self.grid[i][0] != ' ':
                return self.grid[i][0]
            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i] and self.grid[0][i] != ' ':
                return self.grid[0][i]
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] and self.grid[0][0] != ' ':
            return self.grid[0][0]
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] and self.grid[0][2] != ' ':
            return self.grid[0][2]
        return None

    def is_valid_move(self, row, col):
        if row < 0 or row > 2 or col < 0 or col > 2:
            return False
        elif self.grid[row][col] != ' ':
            return False
        return True

    def clear(self):
        self.grid = [[' ' for i in range(3)] for j in range(3)]

    def __str__(self):
        return f"╔═══╦═══╦═══╗\n║ {self.grid[0][0]} ║ {self.grid[0][1]} ║ {self.grid[0][2]} ║\n╠═══╬═══╬═══╣\n║ {self.grid[1][0]} ║ {self.grid[1][1]} ║ {self.grid[1][2]} ║\n╠═══╬═══╬═══╣\n║ {self.grid[2][0]} ║ {self.grid[2][1]} ║ {self.grid[2][2]} ║\n╚═══╩═══╩═══╝"