class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        ans = []

        def backtrack(i, path, total):
            #base case:
            if total == target:
                ans.append(path[:])
                return
            
            #violating cond.
            if i >= len(nums) or total > target:
                return
            
            path.append(nums[i])
            backtrack(i, path, total + nums[i])
            path.pop()
            backtrack(i + 1, path, total)
            return
        
        backtrack(0, [], 0)
        return ans
