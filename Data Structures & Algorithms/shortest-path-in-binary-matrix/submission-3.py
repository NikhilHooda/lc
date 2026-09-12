class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:        
        if grid[0][0] == 1:
            return -1

        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0,1],[-1,1],[1,1],[0,-1],[-1,-1],[1,-1],[-1,0],[1,0]]
        queue = collections.deque()
        queue.append((0,0))
        visit = set()
        visit.add((0,0))

        length = 1
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row < 0 or col < 0 or row >= ROWS or col >= COLS or (row, col) in visit or grid[row][col] == 1:
                        continue
                    queue.append((row, col))
                    visit.add((row, col))
            length += 1
        
        return -1
