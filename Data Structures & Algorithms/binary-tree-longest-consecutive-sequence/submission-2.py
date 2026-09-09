# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(root, parent, curr):
            if not root:
                return
            
            curr = curr + 1 if parent and root.val == parent.val + 1 else 1
            self.ans = max(self.ans, curr)
            dfs(root.left, root, curr)
            dfs(root.right, root, curr)

        dfs(root, None, 0) 
        return self.ans
        
        
        