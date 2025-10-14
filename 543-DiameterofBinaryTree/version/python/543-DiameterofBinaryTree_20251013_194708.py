# Last updated: 10/13/2025, 7:47:08 PM
# recursion to check the length of left and right nodes first. Taking the max of both, adding one and returning to the above node.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            self.diameter = max(self.diameter, left + right)
            return max(left, right) + 1
    
        dfs(root)
        return self.diameter
    