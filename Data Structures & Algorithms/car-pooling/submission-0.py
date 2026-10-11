class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        for passengers, start, end in trips:
            events.append((start, passengers))
            events.append((end, -passengers))
        events.sort()

        passengers = i = 0

        while i < len(events):
            time = events[i][0]
            while i < len(events) and events[i][0] == time:
                passengers += events[i][1]
                i += 1
            if passengers > capacity:
                return False
        
        return True
