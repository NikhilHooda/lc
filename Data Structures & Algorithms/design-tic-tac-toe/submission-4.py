class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = defaultdict(int)
        self.cols = defaultdict(int)
        self.diagonal = 0
        self.anti_diagonal = 0
    
    def move(self, row: int, col: int, player: int) -> int:
        val = -1 if player == 1 else 1
        self.rows[row] += val
        self.cols[col] += val
        if row == col:
            self.diagonal += val
        if col == self.n - row - 1:
            self.anti_diagonal += val
        if (max(abs(self.rows[row]), abs(self.cols[col]), abs(self.diagonal), abs(self.anti_diagonal)) == self.n):
            return player
        
        return 0


    
    


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
