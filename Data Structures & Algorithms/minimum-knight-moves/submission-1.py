class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        directions = [[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1]]

        queue = collections.deque()
        queue.append((0,0))
        visit = set()
        visit.add((0,0))

        moves = 0
        while queue:
            for _ in range(len(queue)): 
                curr_x, curr_y = queue.popleft()

                if (curr_x, curr_y) == (x, y):
                    return moves
                
                for dx, dy in directions:
                    new_x, new_y = curr_x + dx, curr_y + dy
                    if (new_x, new_y) not in visit and new_x >= -2 and new_y >= -2:
                        queue.append((new_x, new_y))
                        visit.add((new_x, new_y))
            moves += 1
            
        