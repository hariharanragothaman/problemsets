# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if root is None:
            return 0
        if not root.left and not root.right:
            return 1
        else:
            max_depth_l = 1 + self.maxDepth(root.left)
            max_depth_r = 1 + self.maxDepth(root.right)  
        return max(max_depth_l, max_depth_r)
