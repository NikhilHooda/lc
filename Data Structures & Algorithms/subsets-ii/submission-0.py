class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        def backtrack(i, path):
            if i == len(nums):
                ans.append(path[:])
                return
            
            path.append(nums[i])
            backtrack(i + 1, path)
            path.remove(nums[i])

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1, path)
            return
        
        backtrack(0, [])
        return ans
        