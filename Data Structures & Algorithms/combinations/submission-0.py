class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(i, path):
            if len(path) == k:
                ans.append(path[:])
                return
            
            for j in range(i, n+1):
                path.append(j)
                backtrack(j+1, path)
                path.pop()
            return



        backtrack(1, [])  
        return ans     