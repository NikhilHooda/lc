class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l + r) // 2
            # left greater
            if m > 0 and nums[m] < nums[m-1]:
                r = m - 1
            # right great
            elif m < len(nums)-1 and nums[m] < nums[m+1]:
                l = m + 1
            # at peak:
            else:
                return m
        