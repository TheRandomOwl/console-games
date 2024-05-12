class Grid:
    # create a grid for connect four
    def __init__(self):
        self.grid = [[' ' for i in range(7)] for j in range(6)]
    
    # method to add a move to the grid
    def add_move(self, col, player):
        for row in self.grid:
            if row[col] == ' ':
                row[col] = player
                break

    def is_valid_move(self, col):
        if col < 0 or col > 6:
            return False
        
        for row in self.grid:
            if row[col] == ' ':
                return True
        return False

    def is_full(self):
        for row in self.grid:
            for cell in row:
                if cell == ' ':
                    return False
        return True
    
    def clear(self):
        self.grid = [[' ' for i in range(7)] for j in range(6)]

    def check_winner(self):
        # check rows
        for row in self.grid:
            for i in range(4):
                if row[i] == row[i+1] == row[i+2] == row[i+3] != ' ':
                    return row[i]

        # check columns
        for i in range(7):
            for j in range(3):
                if self.grid[j][i] == self.grid[j+1][i] == self.grid[j+2][i] == self.grid[j+3][i] != ' ':
                    return self.grid[j][i]

        # check diagonals
        for i in range(3):
            for j in range(4):
                if self.grid[i][j] == self.grid[i+1][j+1] == self.grid[i+2][j+2] == self.grid[i+3][j+3] != ' ':
                    return self.grid[i][j]
                if self.grid[i][j+3] == self.grid[i+1][j+2] == self.grid[i+2][j+1] == self.grid[i+3][j] != ' ':
                    return self.grid[i][j+3]

        return None