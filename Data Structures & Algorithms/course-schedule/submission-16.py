class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adjMap[crs].append(pre)
        
        path, done = set(), set()
        print(adjMap)

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
            return True
    

        for crs in range(numCourses):
            if crs in done:
                continue
            if not dfs(crs):
                return False
        print(done)
        return True
        
        # 0->[1,2]->3