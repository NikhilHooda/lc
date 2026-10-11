"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda i:i.start)
        ends = []
        ans = 0

        for interval in intervals:
            start, end = interval.start, interval.end
            while ends and ends[0] <= start:
                heapq.heappop(ends)
            heapq.heappush(ends, end)
            ans = max(ans, len(ends))
        return ans

