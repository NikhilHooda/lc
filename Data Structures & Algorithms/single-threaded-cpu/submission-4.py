class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)
        tasks.sort(key=lambda t:t[0])
        minHeap, ans = [], []
        time, i = tasks[0][0], 0

        while minHeap or i < len(tasks):
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(minHeap, (tasks[i][1], tasks[i][2]))
                i += 1
            if minHeap:
                processing, idx = heapq.heappop(minHeap)
                ans.append(idx)
                time += processing
            else:
                time = tasks[i][0]
        return ans