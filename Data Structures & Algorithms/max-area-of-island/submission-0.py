class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maxx = 0


        def dfs(r,c):
            if (r < 0 or c < 0 or r >= ROWS or 
               c >= COLS or grid[r][c] == 0):
               return 0
            
            area = 1
            grid[r][c] = 0

            area += dfs(r+1,c)
            area += dfs(r-1,c)
            area += dfs(r,c+1)
            area += dfs(r,c-1)
            return area
        


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    curr = dfs(r,c)
                    maxx = max(maxx, curr)
        
        return maxx   