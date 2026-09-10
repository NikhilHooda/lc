# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []

        hashMap = defaultdict(list) # col# : [node]
        queue = collections.deque()
        queue.append((root, 0))

        
        min_col, max_col = 0, 0
        while len(queue) > 0:
            for i in range(len(queue)):
                node, col = queue.popleft()
                if col < min_col:
                    min_col = col
                elif col > max_col:
                    max_col = col
                hashMap[col].append(node.val)
                if node.left:
                    queue.append((node.left, col-1))
                if node.right:
                    queue.append((node.right, col+1))
        
        return [hashMap[i] for i in range(min_col, max_col + 1)]
            
        