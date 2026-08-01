class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []

        for i in range(len(nums)):
            if not i == 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums)-1
            target = -nums[i]
            while l < r:
                summ = nums[l] + nums[r]
                if summ < target:
                    l += 1
                elif summ > target:
                    r -= 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return ans
