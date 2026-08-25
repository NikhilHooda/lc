class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # [4,5,6,7,0,1,2]

        #cases:
        # left sorted portion (assume mid is 6)
        # target > mid: search right
        # target < l: search right
        # else search left

        # right sorted portion (assume mid is 1)
        # target < mid: search left
        # target > r: search left
        # else search right

        l, r = 0, len(nums)-1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            
            if nums[m] >= nums[l]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        
        return -1

 