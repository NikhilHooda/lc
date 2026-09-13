class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjMap = {i:[] for i in range(n)}
        for parent, child in edges:
            adjMap[parent].append(child)
            adjMap[child].append(parent)
        visit = set()
       
        def dfs(node, parent):
            if node in visit:
                return
            visit.add(node) # {0,1,2}
            for nei in adjMap[node]:
                if nei == parent:
                    continue
                if nei not in visit:
                    dfs(nei, node)
            return

        ans = 0
        parent = -1
        for node in range(n):
            if node not in visit:
                dfs(node, parent)
                ans += 1
        return ans


        