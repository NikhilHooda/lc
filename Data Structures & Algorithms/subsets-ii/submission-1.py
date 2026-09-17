class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        def backtrack(i, path):
            if i == len(nums):
                ans.append(path[:])
                return
            
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i+1, path)
        


        backtrack(0, [])
        return ans