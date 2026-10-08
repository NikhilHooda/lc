class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adjMap[crs].append(pre)
        
        path, done = set(), set()
        order = []

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
            order.append(crs)
            return True
    

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return order
        
        # 0->[1,2]->3
        