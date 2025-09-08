class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        
        mapNum = {}
        for num in nums:
            mapNum[num] = mapNum.get(num, 0) + 1
        
        maxNum = -1
        for num, freq in mapNum.items():
            if freq == 1:
                maxNum = max(maxNum, num)
        
        return maxNum