class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, hashSet = 0, set()
        length = 0

        for r in range(len(s)):
            while s[r] in hashSet:
                hashSet.remove(s[l])
                l += 1
            
            hashSet.add(s[r])
            length = max(length, r - l + 1)
            
        return length
