class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n=len(nums)
        k=len(set(nums))
        freq=[0]*2001
        cnt, winCnt, l=0, 0, 0
        for r, x in enumerate(nums):
            if freq[x]==0: winCnt+=1
            freq[x]+=1
            while l<=r and winCnt==k:
                cnt+=n-r
                freq[nums[l]]-=1
                if freq[nums[l]]==0: winCnt-=1
                l+=1
        return cnt