# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        seen = []

        def dfs(node):
            if not node:
                return 0
            subtree_sum = dfs(node.left) + dfs(node.right) + node.val
            seen.append(subtree_sum)
            return subtree_sum

        total = dfs(root)
        seen.pop()  # remove the sum of the entire tree

        if total % 2 != 0:
            return False
        
        return (total // 2) in seen