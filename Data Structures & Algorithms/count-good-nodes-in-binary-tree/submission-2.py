# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(node, maxVal):
            if not node:
                return 0 
            
            if node.val >= maxVal:
                maxVal = max(maxVal, node.val)
                return 1 + dfs(node.left, maxVal) + dfs(node.right, maxVal)
            return dfs(node.left, maxVal) + dfs(node.right, maxVal)

        return dfs(root, root.val) 
        