class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        # Step 1: Merge adjacent equal elements
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        # Step 2: Shift non-zero elements to the front
        index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[index] = nums[i]
                index += 1

        # Step 3: Fill the rest of the array with zeros
        while index < len(nums):
            nums[index] = 0
            index += 1

        return nums