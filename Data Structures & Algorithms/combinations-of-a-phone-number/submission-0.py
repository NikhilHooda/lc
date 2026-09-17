class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        hashMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(idx, path):
            if idx >= len(digits):
                ans.append(path)
                return
            
            for c in hashMap[digits[idx]]:
                path += c
                backtrack(idx + 1, path)
                path = path[:-1]

        if digits:
            backtrack(0,"")

        return ans
            