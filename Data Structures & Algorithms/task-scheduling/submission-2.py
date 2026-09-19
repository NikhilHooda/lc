class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #heap: [-2,-2]
        #queue: [(-1, 3), (-1, 4)]
        #time: 3

        count = Counter(tasks)
        minHeap = [-cnt for cnt in count.values()]
        heapq.heapify(minHeap)
        queue = collections.deque()
        time = 0

        while minHeap or queue:
            time += 1
            if minHeap:
                cnt = 1 + heapq.heappop(minHeap)
                if cnt:
                    queue.append((cnt, time + n))
            
            if queue and queue[0][1] == time:
                heapq.heappush(minHeap, queue.popleft()[0])
        return time


