class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(idx, path):
            if idx >= len(nums):
                ans.append(path[:])
                return
            
            # no constraints   
            # path 1
            path.append(nums[idx])
            backtrack(idx + 1, path)
            path.remove(nums[idx])
            
            # path 2
            backtrack(idx + 1, path)
            return
        
        backtrack(0, [])
        return ans