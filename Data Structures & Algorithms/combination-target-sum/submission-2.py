class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #base case: sum == target
        #choice: all idxs (including own) and above (nothing behind)
        #constraint, if sum + new_addition >= target then continue
        ans = []
        n = len(nums)
        nums.sort()

        def backtrack(idx, path, total):
            if total == target:
                ans.append(path[:])
                return
            
            for j in range(idx, n):
                new_total = total + nums[j]
                if new_total > target:
                    break
                path.append(nums[j])
                backtrack(j, path, new_total)
                path.remove(nums[j])

        backtrack(0, [], 0)
        return ans