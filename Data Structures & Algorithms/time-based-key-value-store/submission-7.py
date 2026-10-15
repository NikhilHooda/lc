class TimeMap:

    def __init__(self):
        self.valueMap = {} #key: [(1, alice),(2, bob)]
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.valueMap:
            self.valueMap[key] = []
        self.valueMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.valueMap:
            return ""
        
        l, r = 0, len(self.valueMap[key])-1
        ans = ""

        while l <= r:
            m = (l + r) // 2
            if self.valueMap[key][m][0] <= timestamp:
                ans = self.valueMap[key][m][1]
                l = m + 1
            else:
                r = m - 1
        return ans

        
