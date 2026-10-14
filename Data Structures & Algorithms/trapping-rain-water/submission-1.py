class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        lMax, rMax, ans = height[l],height[r],0

        while l < r:
            if lMax <= rMax:
                l += 1
                lMax = max(lMax, height[l])
                ans += lMax - height[l]
            else:
                r -= 1
                rMax = max(rMax, height[r])
                ans += rMax - height[r]
        
        return ans

                          


        