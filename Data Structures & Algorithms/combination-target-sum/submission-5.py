class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(i, path, summ):
            if summ == target:
                ans.append(path[:])
                return
            if i >= len(nums) or summ > target:
                return

            path.append(nums[i])
            backtrack(i, path, summ + nums[i])
            path.pop()
            backtrack(i + 1, path, summ)
            return
        
        backtrack(0, [], 0)
        return ans
        