class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = nums[l]

        while l <= r:
            #sorted array
            if nums[l] < nums[r]:
                res = min(res, nums[l])  
                break  
            #rotated array
            else:
                #min could be the mid element so account for that before splitting
                m = (l + r) // 2
                res = min(res, nums[m])
                #if sorted until mid, then on right array
                if nums[m] >= nums[l]:
                    l = m + 1
                else:
                    r = m - 1
        return res 

                
        
        