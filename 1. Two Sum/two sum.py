
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}  # Dictionary to store number and its index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]  # Return the indices of the two numbers
            num_dict[num] = i  # Add the current number and its index to the dictionary
