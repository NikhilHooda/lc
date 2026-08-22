class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_str = set()
        maxx = 0

        for r in range(len(s)):
            while s[r] in max_str:
                max_str.remove(s[l])
                l += 1
            
            max_str.add(s[r])
            maxx = max(maxx, r-l+1)
        
        return maxx
            

