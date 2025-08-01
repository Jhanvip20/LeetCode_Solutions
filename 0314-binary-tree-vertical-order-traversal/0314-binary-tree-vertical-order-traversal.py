from collections import defaultdict, deque

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        columns = defaultdict(list)
        queue = deque([(root, 0)])
        columns[0] = [root.val]
        
        while queue:
            node, col = queue.popleft()
            
            if node.left:
                queue.append((node.left, col - 1))
                columns[col - 1].append(node.left.val)
                
            if node.right:
                queue.append((node.right, col + 1))
                columns[col + 1].append(node.right.val)
                
        return [columns[x] for x in sorted(columns.keys())]