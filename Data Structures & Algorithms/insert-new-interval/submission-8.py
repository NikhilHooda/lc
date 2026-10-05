class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        n = len(intervals)
        for i in range (len(intervals)):
            if newInterval[0] <= intervals[i][0]:
                intervals.insert(i, newInterval)
                break
            
        if len(intervals) == n:
            intervals.append(newInterval)
        
        merged = [intervals[0]]
        for s, e in intervals:
            end = merged[-1][1]
            if end >= s:
                merged[-1][1] = max(e, end)
            else:
                merged.append([s, e])
        return merged