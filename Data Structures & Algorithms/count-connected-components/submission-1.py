class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjMap = {i:[] for i in range(n)}
        for parent, child in edges:
            adjMap[parent].append(child)
            adjMap[child].append(parent)
        visit = set()
       
        def dfs(node):
            if node in visit:
                return
            visit.add(node) # {0,1,2}
            for nei in adjMap[node]:
                    dfs(nei)
            return

        ans = 0
        for node in range(n):
            if node not in visit:
                dfs(node)
                ans += 1
        return ans


        