from sortedcontainers import SortedDict

class TimeMap:

    def __init__(self):
        self.keyStore = defaultdict(list) ## keyStore = {key: [(value, time)]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyStore[key].append((value, timestamp))
            
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        timestamps = self.keyStore.get(key, [])

        l, r = 0, len(timestamps) - 1
        while l <= r:
            m = (l + r) // 2
            if timestamps[m][1] == timestamp:
                res = timestamps[m][0]
                break
            elif timestamps[m][1] < timestamp:
                res = timestamps[m][0]
                l = m + 1
            else: 
                r = m - 1
        
        return res


        
