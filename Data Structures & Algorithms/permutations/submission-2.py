class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(path):
            if len(path) == len(nums):
                ans.append(path[:])
                return
            
            for num in nums:
                if num in path:
                    continue
                path.append(num)
                backtrack(path)
                path.pop()
            return
        
        backtrack([])
        return ans
