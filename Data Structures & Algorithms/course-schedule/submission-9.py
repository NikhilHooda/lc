class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adjMap[crs].append(pre)
        
        visit = set()

        def dfs(node):
            if node in visit:
                return False
            if adjMap[node] == []:  
                return True

            visit.add(node)
            for nei in adjMap[node]:
                if not dfs(nei):
                    return False
            adjMap[node] = []
            visit.remove(node)
            return True
        

        for node in range(numCourses):
            if not dfs(node):
                return False 
        return True
