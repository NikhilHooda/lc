class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(path, used):
            if len(path) == len(nums):
                ans.append(path[:])
                return
            
            for num in nums:
                if num in used:
                    continue
                path.append(num)
                used.add(num)
                backtrack(path, used)
                path.pop()
                used.remove(num)
            return
        
        backtrack([], set())
        return ans
