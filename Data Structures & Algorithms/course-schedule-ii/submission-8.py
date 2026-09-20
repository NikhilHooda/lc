class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adjMap[crs].append(pre)
        
        ans = []
        visit = set()
        path = set()

        def dfs(node):
            if node in path:
                return False
            if node in visit:
                return True
            path.add(node) 
            for nei in adjMap[node]:
                if not dfs(nei):
                    return False
            path.remove(node)
            visit.add(node)
            ans.append(node)
            return True



        for i in range(numCourses):
            if not dfs(i):
                return []
        return ans
