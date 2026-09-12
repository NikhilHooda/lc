class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adjMap[crs].append(pre)
        visit = set()
        done = set()
        ans = []

        def dfs(crs):
            if crs in visit:
                return False
            if crs in done:
                return True
            
            visit.add(crs)
            for nei in adjMap[crs]:
                if not dfs(nei):
                    return False
            visit.remove(crs)
            done.add(crs)
            ans.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return ans