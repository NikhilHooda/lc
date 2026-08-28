# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = k
        res = root.val

        def dfs(node):
            nonlocal cnt, res
            #once at bottom, return back up
            if not node:
                return 

            #get to leftmost bottom node
            dfs(node.left)
            #if at bottom, and kth smallest already found (cnt == 0) return
            if cnt == 0:
                return
            cnt -= 1
            # if first time finding kth smallest node (cnt == 0) update res
            if cnt == 0:
                res = node.val
            # get to rightmost bottom node
            dfs(node.right)
            return
        
        dfs(root)
        return res
        