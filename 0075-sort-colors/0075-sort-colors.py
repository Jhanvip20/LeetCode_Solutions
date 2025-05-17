class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c0, c1 = 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                c0 += 1
            elif nums[i] == 1:
                c1 += 1

        for i in range(len(nums)):
            if i < c0:
                nums[i] = 0
            elif i >= c0 and i < c0 + c1:
                nums[i] = 1
            else:
                nums[i] = 2    