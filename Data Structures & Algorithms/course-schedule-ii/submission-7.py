class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjMap = {c:[] for c in range(numCourses)}
        for crs, pre in prerequisites:
            adjMap[crs].append(pre)
        path = set()
        done = set()

        def dfs(crs):
            if crs in path:
                return False
            if crs in done:
                return True
            
            path.add(crs)
            for nei in adjMap[crs]:
                if not dfs(nei):
                    return False
            path.remove(crs)
            done.add(crs)
            ans.append(crs)
            return True

        ans = []
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return ans
