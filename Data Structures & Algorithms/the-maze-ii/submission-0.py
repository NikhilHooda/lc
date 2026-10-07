class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        ROWS, COLS = len(maze), len(maze[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        queue = collections.deque()
        visit = set()
        visit.add(tuple(start))
        start.append(0)
        queue.append(start)
        
        min_dist = float("inf")
        while queue:
            r, c, dist = queue.popleft()

            if [r,c] == destination:
                min_dist = min(min_dist, dist)

            print("popped: ", r, c)
            for dr, dc in directions:
                row, col, d = r, c, dist
                while min(row + dr, col + dc) >= 0 and row + dr < ROWS and col + dc < COLS and maze[row + dr][col + dc] != 1:
                    row += dr
                    col += dc
                    d += 1
                
                if (row, col) in visit:
                    continue
                
                print("added: ", row, col)
                queue.append((row, col, d))
                visit.add((row, col))
        

        if min_dist == float("inf"):
            return -1
        else:
            return min_dist