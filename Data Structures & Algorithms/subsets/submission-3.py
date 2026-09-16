class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []


        def backtrack(idx, path):
            #base case
            if idx >= len(nums):
                ans.append(path[:])
                return
            
            #choices
            #include
            path.append(nums[idx])
            backtrack(idx + 1, path)
            path.remove(nums[idx])

            #dont include
            backtrack(idx + 1, path)
            return
    
        backtrack(0, [])
        return ans