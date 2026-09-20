class MedianFinder:

    def __init__(self):
        self.small = [] #maxHeap
        self.large = [] #minHeap 

    def addNum(self, num: int) -> None:
        #always add to small
        heapq.heappush(self.small, -num)

        #check 1: ordering check
        if (self.small and self.large and (-self.small[0] > self.large[0])):
            heapq.heappush(self.large, -heapq.heappop(self.small))
        
        if (self.small and self.large and (self.large[0] < -self.small[0])):
            heapq.heappush(self.small, -heapq.heappop(self.large))
        

        #check 2: length check
        if (len(self.small) - len(self.large)) >= 2:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        
        if (len(self.large) - len(self.small)) >= 2:
            heapq.heappush(self.small, -heapq.heappop(self.large))
        
    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        elif len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return self.large[0]
        

