"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []
        for interval in intervals:
            events.append((interval.start, 1))
            events.append((interval.end, -1))
        
        events.sort()
        best = rooms = i = 0
        while i < len(events):
            rooms += events[i][1]
            best = max(best, rooms)
            i += 1
        return best
