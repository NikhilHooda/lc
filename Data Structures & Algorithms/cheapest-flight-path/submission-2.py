class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjMap = {i:[] for i in range(n)}
        for s, d, price in flights:
            adjMap[s].append([d, price])
        
        
        visit = set()
        self.ans = float("inf")

        def dfs(src, dst, price, k):
            if src == dst:
                self.ans = min(self.ans, price)
                return
            if k < 0 or price >= self.ans:
                return
            visit.add(src)
            for nei, p in adjMap[src]:
                if nei not in visit:
                    dfs(nei, dst, price + p, k-1)
            visit.remove(src)
            return

        dfs(src, dst, 0, k)
        return -1 if self.ans == float("inf") else self.ans