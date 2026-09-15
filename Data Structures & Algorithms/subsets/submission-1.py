class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []


        def backtrack(idx, path):
            # stopping condition
            if idx == len(nums):
                ans.append(path[:])
                return

            # violate constraints

            # choice 1:
            path.append(nums[idx])
            backtrack(idx + 1, path)
            path.pop()

            #choice 2:
            backtrack(idx + 1, path)
            return

        backtrack(0, [])
        return ans