class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        ans = 0
        for r in range(len(prices)):
            if prices[l] > prices[r]:
                l = r
            ans = max(ans, prices[r] - prices[l])

        return ans
