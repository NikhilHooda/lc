class StockSpanner:

    def __init__(self):
        self.stocks = []
        

    def next(self, price: int) -> int:
        self.stocks.append(price)
        last = len(self.stocks)-1
        ans = 0
        while last >= 0 and price >= self.stocks[last]:
            ans += 1
            last -= 1
        return ans


        

        #[100, 80, 60, 70, 60, 75]
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)