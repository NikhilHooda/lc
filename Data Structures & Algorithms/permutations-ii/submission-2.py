class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        count = {n:0 for n in nums}
        for n in nums:
            count[n] += 1

        def backtrack():
            if len(path) == len(nums):
                ans.append(path.copy())
                return
            
            for n in count:
                if count[n] <= 0:
                    continue
                path.append(n)
                count[n] -= 1
                backtrack()
                path.pop()
                count[n] += 1
            
        backtrack()
        return ans
        
        