class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        # outside range
        rng = nums[-1] - nums[0]
        missing = rng - len(nums) + 1
        if missing < k:
            return nums[-1] + k - missing
        
        #inside range (bin search)
        else:
            l, r = 0, len(nums)-1
            while l <= r:
                m = (l + r) // 2
                missing = (nums[m] - nums[0]) - m
                if missing < k:
                    l = m + 1
                else:
                    r = m - 1
        
            return nums[0] + k + l-1