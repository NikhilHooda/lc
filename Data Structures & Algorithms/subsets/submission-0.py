class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def backtrack(idx, path):
            if idx == len(nums):
                ans.append(path[:])
                return
            
            path.append(nums[idx])
            backtrack(idx + 1, path)
            path.pop()

            backtrack(idx + 1, path)
            return
        

        backtrack(0, [])
        return ans

        