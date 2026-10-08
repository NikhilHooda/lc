class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        unique_islands = set()

        def dfs(r,c,direction):
            if (min(r,c) < 0 or r >= ROWS or c >= COLS or (r,c) in visit or grid[r][c] == 0):
                return 
            
            visit.add((r,c))
            path_signature.append(direction)
            dfs(r + 1, c, "D")
            dfs(r - 1, c, "U")
            dfs(r, c + 1, "R")
            dfs(r, c - 1, "L")
            path_signature.append("0")

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visit and grid[r][c] == 1:
                    path_signature = []
                    dfs(r,c,"0")
                    unique_islands.add(tuple(path_signature))
        
        return len(unique_islands)
        