class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r  = 0, 0
        ans = 0
        while r < len(prices):
            #profitable?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                ans = max(ans, profit)
            else:
                l = r
            r += 1
      
        return ans
