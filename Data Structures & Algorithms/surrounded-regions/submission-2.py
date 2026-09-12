class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        def dfs(r,c):
            if (min(r,c) < 0 or r == ROWS or c == COLS 
                or board[r][c] != "O"):
                return
            
            board[r][c] = "#"
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            return
        
        # 1. everything but unsurrounded regions (border "O"s to "#"s):
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O" and 
                   (r in [0, ROWS-1] or c in [0, COLS-1])):
                    dfs(r,c)
        # 2. capture surrounded regions (inner "O"s to "X"s):
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O"):
                    board[r][c] = "X"
        # 3. convert "#"s back to "O"s):
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "#"):
                    board[r][c] = "O"
            

        