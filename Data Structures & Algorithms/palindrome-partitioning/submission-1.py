class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def backtrack(i, path):
            if i >= len(s):
                ans.append(path[:])
            
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    path.append(s[i:j+1])
                    backtrack(j+1, path)
                    path.pop()
            return
        
        backtrack(0, [])
        return ans

    def isPali(self, s, l ,r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True