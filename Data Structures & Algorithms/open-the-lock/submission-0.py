class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = collections.deque()
        queue.append("0000")
        visit = set()
        for deadend in deadends:
            if deadend == "0000":
                return -1
            visit.add(deadend)
        
        length = 0 
        while queue:
            for _ in range(len(queue)):
                code = queue.popleft()
                if code in visit:
                    continue 
                if code == target: 
                    return length
                
                visit.add(code)
                for i in range(4):
                    digit = int(code[i])
                    for new in [(digit + 1) % 10, (digit + 9) % 10]:
                        combo = code[:i] + str(new) + code[i+1:]
                        queue.append(combo)
            length += 1

        return -1

        