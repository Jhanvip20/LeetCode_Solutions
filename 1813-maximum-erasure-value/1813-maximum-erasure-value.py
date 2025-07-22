class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        hasX=[False]*(max(nums)+1)
        ans, wsum=0, 0
        l, r=0, 0
        for l, x in enumerate(nums):
            while r<n and not hasX[(y:=nums[r])]:
                hasX[y]=True
                wsum+=y
                r+=1
            ans=max(ans, wsum)
            hasX[x]=False
            wsum-=x
            if r>=n-1: break
        return ans
        