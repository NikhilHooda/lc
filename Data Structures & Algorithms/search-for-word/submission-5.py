class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        directions = [[0,1], [0,-1],[1,0],[-1,0]]
        visit = set()

        def dfs(idx,r,c):
            if idx == len(word):
                return True
            
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if (min(row, col) < 0 or row >= ROWS or col >= COLS or (row,col) in visit or board[row][col] != word[idx]):
                    continue
                visit.add((row, col))
                if dfs(idx + 1, row, col):
                    return True
                visit.remove((row, col))
            return False
     
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    visit.add((r,c))
                    if dfs(1,r,c):
                        return True
                    visit.remove((r,c))
        return False