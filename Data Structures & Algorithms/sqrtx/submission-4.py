class Solution:
    def mySqrt(self, x: int) -> int:
        l, r, ans = 0, x, 0


        while l <= r:
            mid = (l + r) // 2
            sqr = mid * mid
            if sqr < x:
                l = mid + 1
                ans = mid
            elif sqr > x:
                r = mid - 1
            else:
                return mid
        return ans