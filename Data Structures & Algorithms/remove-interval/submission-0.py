class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        remove_start, remove_end = toBeRemoved
        output = []

        for start, end in intervals:
            if start > remove_end or end < remove_start:
                output.append([start, end])
            else:
                if start < remove_start:
                    output.append([start, remove_start])
                if end > remove_end:
                    output.append([remove_end, end])
                
        return output

        