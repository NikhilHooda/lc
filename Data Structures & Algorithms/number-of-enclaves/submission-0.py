class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        def dfs(r,c):
            if (min(r,c) < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0):
                return
            
            grid[r][c] = 0
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            return
        
        # replace all 1s reachable from boundary with 0s
        for r in range(ROWS):
            for c in range(COLS):
                if (grid[r][c] == 1 and (r in [0,ROWS-1] or c in [0,COLS-1])):
                    dfs(r,c)
        
        ans = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1: 
                    ans += 1
        return ans

        