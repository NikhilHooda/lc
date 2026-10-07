class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        visit = set()

        #dfs on any boundary 1's and add them to visited
        def dfs(r,c):
            if(min(r,c) < 0 or r >= ROWS or c >= COLS or (r,c) in visit or grid[r][c] == 0):
                return 
            
            visit.add((r,c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            return
        
        for r in range(ROWS):
            for c in range(COLS):
                if (grid[r][c] == 1 and 
                   (r in (0, ROWS-1) or c in (0, COLS-1))):
                   dfs(r,c)
        
        print(visit)
        # find all 1s not in visit
        enclaves = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visit and grid[r][c] == 1:
                    enclaves += 1
        return enclaves
