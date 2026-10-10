class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visit = set()

        def dfs(node):
            if node in visit:
                return

            visit.add(node)
            for nei in range(n):
                if isConnected[node][nei]:
                    dfs(nei)
            return 

        provinces = 0
        for node in range(n):
            if node not in visit:
                dfs(node)
                provinces += 1
        return provinces
        