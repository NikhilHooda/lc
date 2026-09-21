class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # a -> b -> c ab -> bc
        adjMap = defaultdict(list)
        for i in range(len(equations)):
            adjMap[equations[i][0]].append([equations[i][1], values[i]])
            adjMap[equations[i][1]].append([equations[i][0], 1 / values[i]])
        

        def dfs(node, target, product, visit):
            if node not in adjMap or target not in adjMap:
                return False
            if node == target:
                ans.append(product)
                return True
            visit.add(node)
            for nei, p in adjMap[node]:
                if nei not in visit:
                    if dfs(nei, target, product * p, visit):
                        return True
            visit.remove(node)
            return False
        
        ans = []
        for node, target in queries:
            if not dfs(node, target, 1.0, set()):
                ans.append(-1.0)
        return ans