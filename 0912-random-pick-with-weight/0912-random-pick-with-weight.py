import bisect

class Solution:

    def __init__(self, w: List[int]):
        for idx in range(len(w) - 1):
            w[idx + 1] = w[idx] + w[idx + 1]
        self.w = w

    def pickIndex(self) -> int:
        random_int = randint(0, self.w[-1] - 1)
        return bisect.bisect_right(self.w, random_int)
        # return self.num_indexes[randint(0, len(self.weighted_array) - 1)]
    
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()