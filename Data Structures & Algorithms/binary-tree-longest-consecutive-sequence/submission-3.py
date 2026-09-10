# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node, parent, curr):
            if not node:
                return
            
            curr = curr + 1 if parent and node.val == parent.val + 1 else 1
            self.ans = max(self.ans, curr)
            dfs(node.left, node, curr) 
            dfs(node.right, node, curr) 
            return
        

        dfs(root, None, 1)
        return self.ans