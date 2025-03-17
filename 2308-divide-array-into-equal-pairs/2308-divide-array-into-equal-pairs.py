class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums.sort()  # Sort the array
        for i in range(0, len(nums), 2):
            if nums[i] != nums[i + 1]:  # Check pairs
                return False
        return True 