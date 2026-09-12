class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        ROWS, COLS = len(heights), len(heights[0])
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    pac.add((r,c))
                if r == ROWS-1 or c == COLS-1:
                    atl.add((r,c))
        
        def bfs(ocean):
            queue = collections.deque()
            for r,c in ocean:
                queue.append((r,c))
            directions = [[0,1], [0,-1], [1,0], [-1,0]]

            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row < 0 or col < 0 or row >= ROWS or 
                       col >= COLS or (row, col) in ocean):
                        continue
                    if heights[r][c] <= heights[row][col]:
                        ocean.add((row, col))
                        queue.append((row, col))
            return
        bfs(pac)
        bfs(atl)
        return [[r, c] for r, c in pac & atl]

        