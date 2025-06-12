class Solution(object):
    def maxAdjacentDistance(self, nums):
        diff = 0
        counter = 1

        for i in range(len(nums)):
            if counter == len(nums):
                counter = 0
            
            temp = abs(nums[i] - nums[counter])
            if temp > diff:
                diff = temp
            
            counter += 1

        return diff