class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = r
        while l <= r:
            speed = (l + r) // 2
            tmp = 0
            for pile in piles:
                tmp += math.ceil(pile/speed)
            if tmp > h:
                l = speed + 1
            else:
                ans = min(ans, speed)
                r = speed - 1
        
        return ans

        