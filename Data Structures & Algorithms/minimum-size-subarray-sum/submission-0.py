class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, res = 0, len(nums)+1
        summ, length = 0, 0

        for r in range(len(nums)):
            if summ < target:
                summ += nums[r]
                length += 1
            while summ >= target:
                res = min(res, length)
                summ -= nums[l]
                l += 1
                length -= 1

        if res == len(nums)+1:
            return 0
        else:
            return res      
