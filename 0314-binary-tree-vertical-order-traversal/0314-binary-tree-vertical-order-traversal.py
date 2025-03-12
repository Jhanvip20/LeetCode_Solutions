# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Dictionary to store nodes grouped by their vertical column index
        cols = collections.defaultdict(list)
        queue = collections.deque([(root, 0)]) # Initialize queue for BFS traversal, storing (node, column index)
        while queue:
            node, i = queue.popleft() # Dequeue element
            if node:
                cols[i].append(node.val) # Store node value in the corresponding column index
                # Add left child to queue with column index decreased by 1
                # Add right child to queue with column index increased by 1
                queue += (node.left, i - 1), (node.right, i + 1) 
        return [cols[i] for i in sorted(cols)] # Return a list of node values in sorted column order