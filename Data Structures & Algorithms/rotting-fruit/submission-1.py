class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions =[[0,1],[0,-1],[1,0],[-1,0]]
        fresh = 0
        queue = collections.deque()
        visit = set()


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r,c))
                    visit.add((r,c))
        
        time = 0
        while queue and fresh:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row < 0 or col < 0 or row >= ROWS or col >= COLS or (row, col) in visit or grid[row][col] == 0: 
                        continue

                    queue.append((row, col))
                    visit.add((row, col))
                    fresh -= 1
            time += 1

        if fresh:
            return -1
        return time



        