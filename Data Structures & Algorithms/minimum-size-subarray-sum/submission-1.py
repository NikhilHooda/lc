class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, res = 0, len(nums)+1
        summ = 0

        for r in range(len(nums)):
            if summ < target:
                summ += nums[r]
            while summ >= target:
                res = min(res, r-l+1)
                summ -= nums[l]
                l += 1

        if res == len(nums)+1:
            return 0
        else:
            return res      
