class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjMap = { i:[] for i in range(n) }
        for parent, child in edges:
            adjMap[parent].append(child)
            adjMap[child].append(parent)
        visit = set()
        print(adjMap)

        def dfs(node, parent):
            if node in visit:
                return False

            visit.add(node)
            for nei in adjMap[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True


        return dfs(0,-1) and len(visit) == n