from sortedcontainers import SortedDict

class TimeMap:

    def __init__(self):
        self.store = {} # key : list of [value, timestamp] pairs

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        values = self.store.get(key, [])

        #binary search
        l, r = 0, len(values)-1

        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] < timestamp:
                ans = values[mid][0]
                l = mid + 1
            elif values[mid][1] > timestamp:
                r = mid - 1
            else:
                ans = values[mid][0]
                break
        return ans



        
