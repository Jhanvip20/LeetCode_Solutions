class Solution:
    def goodTriplets(self, nums1, nums2):
        n = len(nums1)
        pos2 = {nums2[i]: i for i in range(n)}

        # Map nums1[i] to its position in nums2
        mapped = [pos2[nums1[i]] for i in range(n)]

        bitLeft = BIT(n)
        bitRight = BIT(n)
        rightCount = [0] * n

        # Count right side first
        for i in range(n - 1, -1, -1):
            rightCount[i] = bitRight.query(n - 1) - bitRight.query(mapped[i])
            bitRight.update(mapped[i], 1)

        result = 0

        # Count left and calculate triplets
        for i in range(n):
            left = bitLeft.query(mapped[i] - 1)
            right = rightCount[i]
            result += left * right
            bitLeft.update(mapped[i], 1)

        return result


class BIT:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 2)

    def update(self, index, delta):
        index += 1
        while index <= self.size + 1:
            self.tree[index] += delta
            index += index & -index

    def query(self, index):
        result = 0
        index += 1
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result
        