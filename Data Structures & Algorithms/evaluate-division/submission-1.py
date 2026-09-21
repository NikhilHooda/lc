class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # a -> b -> c ab -> bc
        adjMap = defaultdict(list)
        for i in range(len(equations)):
            adjMap[equations[i][0]].append([equations[i][1], values[i]])
            adjMap[equations[i][1]].append([equations[i][0], 1 / values[i]])
        

        def bfs(src, target):
            if src not in adjMap or target not in adjMap:
                return -1
            queue, visit = collections.deque([(src, 1)]), set()
            visit.add(src)

            while queue:
                node, w = queue.popleft()
                if node == target:
                    return w
                
                for nei, weight in adjMap[node]:
                    if nei not in visit:
                        queue.append((nei, w * weight))
                        visit.add(nei)
            return -1

        ans = []
        for node, target in queries:
            ans.append(bfs(node, target))
        return ans