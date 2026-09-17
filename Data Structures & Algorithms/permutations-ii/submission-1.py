class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        def backtrack(path):
            if len(path) == len(nums):
                ans.append(path[:])
                return
            
            for num in count:
                if count[num] == 0:
                    continue
                path.append(num)
                count[num] -= 1
                backtrack(path)
                path.pop()
                count[num] += 1
            return
        
        backtrack([])
        return ans