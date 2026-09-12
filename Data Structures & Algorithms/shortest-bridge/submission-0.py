class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        visit = set()
        #dfs to find one island
        def dfs(r,c):
            if (min(r,c) < 0 or r >= ROWS or c >= COLS or (r,c) in visit or grid[r][c] == 0):
                return
            visit.add((r,c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        found = False
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs(r, c)
                    found = True
                    break
            if found:
                break
        
        #bfs to find shortest path from this island to next one
        queue = collections.deque()
        for r,c in visit:
            queue.append((r,c))
        
        ans = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if min(row,col) < 0 or row >= ROWS or col >= COLS or (row,col) in visit:
                        continue
                    
                    if grid[row][col] == 1:
                        return ans
                    queue.append((row, col))
                    visit.add((row, col))
            ans += 1
                
        
        