class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #heap: -2,-2
        #queue: (-1, 3)
        #time = 3

        counter = {}
        for c in tasks:
            counter[c] = 1 + counter.get(c, 0)
        
        heap = [-cnt for cnt in counter.values()]
        heapq.heapify(heap)
        queue = collections.deque()
        time = 0

        while heap or queue:
            time += 1
            if heap:
                cnt = 1 + heapq.heappop(heap)
                if cnt:
                    queue.append((cnt, time + n))
            
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])
        return time
        
        