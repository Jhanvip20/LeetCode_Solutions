class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        nidx=[]
        for i, x in enumerate(nums):
            nidx.append((x, i))
        nidx.sort(reverse=True)
        return [info[0] for info in sorted(nidx[:k], key=lambda info: info[1])]
        