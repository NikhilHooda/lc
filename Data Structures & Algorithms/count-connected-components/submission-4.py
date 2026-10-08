class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjMap = {i:[] for i in range(n)}
        for src, dest in edges:
            adjMap[src].append(dest)
            adjMap[dest].append(src)
        visit = set()

        def dfs(node):
            if node in visit:
                return
            
            visit.add(node)
            for nei in adjMap[node]:
                if nei not in visit:
                    dfs(nei)
            return

        components = 0
        for node in range(n):
            if node not in visit:
                dfs(node)
                components += 1
        return components