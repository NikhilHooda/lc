class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        row_count, col_count = [0] * ROWS, [0] * COLS

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    row_count[r] += 1
                    col_count[c] += 1   

        ans = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (row_count[r] > 1 or col_count[c] > 1):
                    ans += 1
        return ans      
        