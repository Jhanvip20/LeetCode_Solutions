# class for a node of the segment tree
class TreeNode:
    def __init__(self, val = None, left = None, right = None, positions = None):
        self.left = left
        self.right = right
        #this variable holds the minimum value of the segment
        self.minVal = val
        #this variable holds the positions of the minima
        self.positions = [] if positions is None else positions

# class for the segment tree
class SegmentTree:
    def __init__(self, array):
        self.n = len(array)
        self.root = self.build(array)

    def build(self, array, left=0, right = None):
        if right is None:
            right = self.n - 1
        
        if left == right:
            return TreeNode(val = array[left], positions=[left])
        
        node = TreeNode()
        mid = (left + right) // 2
        leftChild = self.build(array, left, mid)
        rightChild = self.build(array, mid + 1, right)
        node.left, node.right = leftChild, rightChild
        if leftChild.minVal < rightChild.minVal:
            node.minVal, node.positions = leftChild.minVal, list(leftChild.positions)
        elif rightChild.minVal < leftChild.minVal:
            node.minVal, node.positions = rightChild.minVal, list(rightChild.positions)
        else:
            #if both children had equal minimum, we join the lists of positions
            node.minVal = leftChild.minVal
            node.positions = leftChild.positions + rightChild.positions
        return node
        

    def query(self, ltarget, rtarget, l=0, r=None, node=None):
        if r == None:
            r = self.n - 1
        if node == None:
            node = self.root
        
        if ltarget == l and rtarget == r:
            return node.minVal, node.positions

        mid = (l+r) // 2
        if rtarget <= mid:
            return self.query(ltarget, rtarget, l, mid, node.left)
        elif ltarget > mid:
            return self.query(ltarget, rtarget, mid + 1, r, node.right)
        else:
            lminVal, lpos = self.query(ltarget, mid, l, mid, node.left)
            rminVal, rpos = self.query(mid + 1, rtarget, mid + 1, r, node.right)
            if lminVal < rminVal:
                return lminVal, lpos
            elif rminVal < lminVal:
                return rminVal, rpos
            else:
                return lminVal, lpos + rpos
    

# main solution
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)
        stree = SegmentTree(target)

        # this stack will hold all the subarrays that we need to visit and their value
        # format of a subarray: (left_bound, right_bound, current_value)
        intervals = [(0, n-1, 0)]

        operations = 0
        while intervals:
            left, right, val = intervals.pop()
            if right < left:
                continue

            # obtaining the minima and their positions from seg tree
            intervalMin, minPos = stree.query(left, right) 
            operations += (intervalMin - val) 
            val = intervalMin
            # splitting the subarray around the minima
            for breakPoint in minPos:
                intervals.append((left, breakPoint - 1, val))  # adding to stack
                left = breakPoint + 1
            if right >= left:
                intervals.append((left, right, val))  # adding last interval to stack

        return operations