class StockSpanner:

    def __init__(self):
        self.stocks = []
        

    def next(self, price: int) -> int:
        self.stocks.append(price)
        stack = [0] * len(self.stocks)
        for i in range(len(self.stocks)):
            stack[i] = self.stocks[i]
        ans = 0
        while stack and stack[-1] <= price:
            stack.pop()
            ans += 1
        return ans


        

        #[100, 80, 60, 70, 60, 75]
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)