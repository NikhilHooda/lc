# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(minHeap, (node.val, i, node))
        
        dummy = ListNode(0)
        cur = dummy
        while minHeap:
            val, idx, node = heapq.heappop(minHeap)
            cur.next = node
            cur = cur.next
            node = node.next
            if node:
                heapq.heappush(minHeap, (node.val, idx, node))
        return dummy.next
        