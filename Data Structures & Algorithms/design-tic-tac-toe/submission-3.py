class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.board = [[0] * n for _ in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player

        if ((self.check_rows(row, player)) or 
            (self.check_cols(col, player)) or 
            (row == col and self.check_diagonal(player)) or 
            (col == self.n - row - 1 and self.check_anti_diagonal(player))):
            return player
        
        return 0

    def check_rows(self, row, player):  
        for c in range(self.n):
            if self.board[row][c] != player:
                return False
        return True

    def check_cols(self, col, player): 
        for r in range(self.n):
            if self.board[r][col] != player:
                return False
        return True

        #diagonal
    def check_diagonal(self, player): 
        for r in range(self.n):
            if self.board[r][r] != player:
                return False
        return True

        #anti_diagonal
    def check_anti_diagonal(self, player):        
        for r in range(self.n):
            if self.board[r][self.n - r - 1] != player:
                return False
        return True

    
    


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
