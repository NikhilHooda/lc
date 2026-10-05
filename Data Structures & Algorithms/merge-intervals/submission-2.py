class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda k: k[0])

        merged = [intervals[0]]
        for s, e in intervals:
            end = merged[-1][1]
            if end >= s:
                merged[-1][1] = max(e, merged[-1][1])
            else:
                merged.append([s, e])
        return merged
        