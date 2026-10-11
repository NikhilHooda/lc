class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intersection = []
        l1 = l2 = 0
        while l1 < len(firstList) and l2 < len(secondList):
            first_start, first_end = firstList[l1]
            second_start, second_end = secondList[l2]

            start = max(first_start, second_start)
            end = min(first_end, second_end)

            if start <= end:
                intersection.append([start, end])
            
            if first_end < second_end:
                l1 += 1
            else:
                l2 += 1

        return intersection 
        