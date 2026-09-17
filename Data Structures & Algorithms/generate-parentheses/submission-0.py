class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        openN = 0
        closedN = 0

        
        def backtrack(path, openN, closedN):
            if openN == closedN == n:
                ans.append(path)
                return
            
            if openN < n:
                path += "("
                backtrack(path, openN + 1, closedN)
                path = path[:-1]
            
            if closedN < openN:
                path += ")"
                backtrack(path, openN, closedN + 1)
                path = path[:-1]
            return

    
        backtrack("", 0, 0)
        return ans
        