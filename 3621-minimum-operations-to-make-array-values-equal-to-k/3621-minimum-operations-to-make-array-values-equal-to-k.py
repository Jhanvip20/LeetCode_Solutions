class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # if there is a number $x$ that is less than $k$,
        # then return -1
        if any(x < k for x in nums): return -1
        # otherwise check the size of the unique number that is greater than k
        return len(set(x for x in nums if x > k))