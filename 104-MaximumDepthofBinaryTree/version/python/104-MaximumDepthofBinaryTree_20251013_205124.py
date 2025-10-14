# Last updated: 10/13/2025, 8:51:24 PM
'''
very similar to diameter of a binary tree. 

Here we just find the max depth of the left or right subtree and return the max.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0

        def depth(node):
            nonlocal res
            if not node:
                return 0
            
            left = depth(node.left)
            right = depth(node.right)

            res = max(left, right) + 1
            return res
            
        depth(root)
        return res