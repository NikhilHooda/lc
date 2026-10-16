class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(i, path):
            if i == len(nums):
                ans.append(path.copy())
                return
        
            #decision
            path.append(nums[i])
            #recurse
            backtrack(i + 1, path)
            #undo decision
            path.pop()
            backtrack(i + 1, path)
        
        backtrack(0, [])
        return ans
