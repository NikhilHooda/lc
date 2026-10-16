class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(path, used):
            if len(path) == len(nums):
                ans.append(path[:])
                return
            
            for i in range(len(nums)):
                if nums[i] in used:
                    continue
                path.append(nums[i])
                used.add(nums[i])
                backtrack(path, used)
                path.pop()
                used.remove(nums[i])
        
        backtrack([], set())
        return ans