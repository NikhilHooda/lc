class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #max heap of k smallest points
        heap = []
        heapq.heapify(heap)
        for x,y in points:
            dist = -(x**2 + y**2)
            heapq.heappush(heap, (dist, [x, y]))
            if len(heap) > k:
                heapq.heappop(heap)
        
        ans = []
        for dist, points in heap:
            ans.append(points)
        return ans

        