# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # path sum = max of left + max of right
        # get path sum at EACH node
        # up each path return the current node val (if above 0) + max(left, right)  
        self.path_sum = root.val

        def dfs(root):
            if not root:
                return 0   
            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)
            self.path_sum = max(self.path_sum, root.val + left + right) 
            return root.val + max(left, right)
        
        dfs(root)
        return self.path_sum
        