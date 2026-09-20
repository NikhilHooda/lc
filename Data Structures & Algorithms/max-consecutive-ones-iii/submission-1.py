class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, ones, ans = 0, 0, 0     

        for r in range(len(nums)):
            if nums[r] == 1:
                ones += 1
            if ((r-l+1) - ones) > k:
                if nums[l] == 1:
                    ones -= 1
                l += 1
            ans = max(ans, r-l+1)
        return ans

        