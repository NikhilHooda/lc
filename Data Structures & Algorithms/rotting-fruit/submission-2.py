class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        queue = collections.deque()
        time = 0
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))
        
        while queue and fresh:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (min(row, col) < 0 or row >= ROWS or col >= COLS or grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    queue.append((row, col))
                    fresh -= 1
            time += 1
        
        if fresh:
            return -1
        return time



        