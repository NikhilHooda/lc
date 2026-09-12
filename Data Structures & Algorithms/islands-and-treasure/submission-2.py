class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        queue = collections.deque()
        visit = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append([r, c])
                    visit.add((r, c))
        length = 1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (min(row, col) < 0 or row >= ROWS or col >= COLS or (row, col) in visit or grid[row][col] == -1):
                        continue
                    
                    grid[row][col] = length
                    queue.append((row, col))
                    visit.add((row, col))
            length += 1
        

                


