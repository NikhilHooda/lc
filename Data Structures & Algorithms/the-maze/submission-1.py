class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        ROWS, COLS = len(maze), len(maze[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        queue = collections.deque()
        queue.append(start)
        visit = set()
        visit.add(tuple(start))

        while queue:
            r, c = queue.popleft()

            if [r,c] == destination: 
                return True
            
            for dr, dc in directions:
                row, col = r, c
                while min(row + dr, col + dc) >= 0 and row + dr < ROWS and col + dc < COLS and maze[row + dr][col + dc] != 1:
                    row += dr
                    col += dc
                
                if (row, col) in visit:
                    continue
                
                queue.append((row, col))
                visit.add((row, col))

        return False

        