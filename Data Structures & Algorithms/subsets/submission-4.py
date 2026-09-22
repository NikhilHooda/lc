class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(idx, path):
            if idx == len(nums):
                ans.append(path[:])
                return
            
            #choice 1
            path.append(nums[idx])
            dfs(idx + 1, path)
            path.pop()

            #choice 2
            dfs(idx+1, path)
        

        dfs(0, [])
        return ans