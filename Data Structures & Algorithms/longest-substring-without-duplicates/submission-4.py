class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, hashset = 0, set()
        length = 0

        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            else:
                hashset.add(s[r])
                length = max(length, r-l+1)
        
        return length