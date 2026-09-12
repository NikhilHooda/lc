class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adjMap[crs].append(pre)
        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            
            visit.add(crs)
            for nei in adjMap[crs]:
                if not dfs(nei):
                    return False
            adjMap[crs] = []
            visit.remove(crs) 
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True

        