class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = [(38, 1),(36,3)]
        ans = [[1,0,1,0,0,0,0]]

        stack = []
        ans = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                temperature, idx = stack.pop()
                ans[idx] = i - idx
            stack.append((temp, i))
        return ans
        