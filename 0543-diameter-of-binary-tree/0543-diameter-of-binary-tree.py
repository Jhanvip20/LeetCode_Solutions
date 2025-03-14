# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0 # Member variable to store the diameter

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.helper(root)
        return self.diameter # Return the calculated diameter

    def helper(self, node: TreeNode) -> int:
        if not node:
            return 0 # Base case: if node is null, return 0

        left_depth = self.helper(node.left)   # Get depth of left subtree
        right_depth = self.helper(node.right) # Get depth of right subtree

        # Calculate diameter at this node (number of edges)
        current_diameter = left_depth + right_depth

        # Update the maximum diameter found so far
        self.diameter = max(self.diameter, current_diameter)

        # Return the depth of this subtree
        return max(left_depth, right_depth) + 1
