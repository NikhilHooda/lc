class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []

        def backtrack(i):
            if i >= len(s):
                ans.append(path.copy())
            
            for j in range(i, len(s)):
                if self.ispali(s, i, j):
                    path.append(s[i:j+1])
                    backtrack(j+1)
                    path.pop()
        
        backtrack(0)
        return ans
    
    def ispali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True

    
