class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []


        def backtrack(path, path_set):
            #base case:
            if len(path_set) == 0:
                ans.append(path[:])
            
            for num in list(path_set):
                path.append(num)
                path_set.remove(num)
                backtrack(path, path_set)
                path.pop()
                path_set.add(num)
            return

        backtrack([], set(nums))
        return ans
        