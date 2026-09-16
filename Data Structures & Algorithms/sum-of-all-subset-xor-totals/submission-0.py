class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.ans = 0



        def backtrack(idx, path):
            if idx >= len(nums):
                result = 0
                for num in path:
                    result ^= num
                self.ans += result
                return
            
            path.append(nums[idx])
            backtrack(idx + 1, path)
            path.remove(nums[idx])

            backtrack(idx + 1, path)
            return

        backtrack(0, [])
        return self.ans
        