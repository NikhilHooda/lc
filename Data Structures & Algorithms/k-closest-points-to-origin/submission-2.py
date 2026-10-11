class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #min-heap of size k
        minHeap = []
        for point in points:
            x,y = point
            dist = x**2 + y**2
            minHeap.append((dist, x, y))
        
        heapq.heapify(minHeap)
        ans = []
        while len(ans) < k:
            _, x, y = heapq.heappop(minHeap)
            ans.append([x,y])
        return ans

        
        