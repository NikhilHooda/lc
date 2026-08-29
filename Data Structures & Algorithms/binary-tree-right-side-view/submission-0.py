# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # level 0: [1]
        # level 1: [2,3]
        # level 2: [4,5]
        queue = collections.deque()
        ans = []

        if root:
            queue.append(root)
        
        while len(queue) > 0:
            ans.append(queue[-1].val) #add rightmost val in queue to answer
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return ans

        