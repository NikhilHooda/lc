class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        max_area = 0
        visit = set()

        def dfs(r,c):
            if (min(r,c) < 0 or r >= ROWS or c >= COLS or (r,c) in visit or grid[r][c] == 0):
                return 0
            visit.add((r,c))
            count = 1
            for dr, dc in directions:
                count += dfs(r + dr, c + dc)
            return count
            
        


        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visit and grid[r][c] == 1:
                    max_area = max(max_area, dfs(r,c))
        
        return max_area

