class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMap = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in hashMap:
                if stack and stack.pop() == hashMap[c]:
                    continue
                else:
                    return False
            stack.append(c)
        
        if len(stack) == 0:
            return True
        return False
