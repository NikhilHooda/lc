class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        ans = nums[l]

        while l <= r:
            m = (l + r) // 2
            #sorted array
            if nums[l] < nums[r]:
                ans = min(ans, nums[l])
                
            #rotated array
            # case 1: curr is minimum
            ans = min(ans, nums[m])
            # case 2: left sorted half
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return ans
        