class SparseVector:
    def __init__(self, nums: List[int]):
        self.ix = {i: x for i, x in enumerate(nums) if x}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        a, b = self.ix, vec.ix
        return sum(a[i] * b[i] for i in a if i in b)

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)