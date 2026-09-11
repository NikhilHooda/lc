class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        queue = collections.deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        length = 0
        while queue and fresh:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    if (min(r + dr, c + dc) < 0 or (r + dr) >= ROWS or 
                           (c + dc) >= COLS or grid[r + dr][c + dc] == 0 or
                            grid[r + dr][c + dc] == 2):
                            continue
                    grid[r + dr][c + dc] = 2
                    fresh -= 1
                    queue.append((r + dr,c + dc))
            length += 1
        
        if fresh:
            return -1
        return length




        