class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        adjMap = {i:[] for i in range(n)}
        for src, dest in edges:
            adjMap[src].append(dest)
        visit = set()
        
        def dfs(node):
            if not adjMap[node]:
                return node == destination
            if node in visit:
                return False
                
            visit.add(node)
            for nei in adjMap[node]:
                if not dfs(nei):
                    return False
            visit.remove(node)
            return True
            
        return dfs(source)