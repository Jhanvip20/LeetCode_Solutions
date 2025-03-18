class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        mask=0
        max1=0
        i=0 # left
        for j in range(len(nums)):  #right
            while((mask & nums[j])!=0):
                mask^=nums[i]  
                i+=1
            mask |=nums[j]
            max1=max(max1,j-i+1)
        
        return max1