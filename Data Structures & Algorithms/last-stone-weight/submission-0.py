import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        
        heapq.heapify(stones)

        while len(stones) > 1:
            s1, s2 = heapq.heappop(stones), heapq.heappop(stones)
            if -s1 > -s2:
                heapq.heappush(stones, s1 - s2)
            elif s1 == s2:
                continue
        
        if stones:
            for i in range(len(stones)):
                stones[i] = -stones[i] 
            return stones[-1]
        return 0
        
    
        