class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        best = r
        while l <= r:
            rate = (l + r) // 2
            tmp = 0
            for pile in piles:
                tmp += math.ceil(pile / rate)
            if tmp <= h:
                r = rate - 1
                best = min(best, rate)
            else:
                l = rate + 1
        
        return best
        

        