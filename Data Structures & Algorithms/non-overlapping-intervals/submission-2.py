class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        merged = [intervals[0]]
        output = 0

        for start, end in intervals[1:]:
            if merged and merged[-1][1] > start:
                output += 1
                merged[-1][1] = min(end, merged[-1][1])
            else:
                merged.append([start, end])
        return output



        