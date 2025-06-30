"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        prev = None
        head = None

        def dfs(node):
            nonlocal prev, head
            if not node:
                return
            # Traverse left
            dfs(node.left)

            # Link prev <-> node
            if prev:
                prev.right = node
                node.left = prev
            else:
                # This is the leftmost (smallest) node
                head = node

            prev = node  # move prev forward

            # Traverse right
            dfs(node.right)

        dfs(root)

        # Close the circular list
        head.left = prev
        prev.right = head

        return head