class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_than = []
        equal_to = []
        greater_than = []
        
        # Categorize each element in the array
        for num in nums:
            if num < pivot:
                less_than.append(num)
            elif num == pivot:
                equal_to.append(num)
            else:
                greater_than.append(num)
        
        # Return the concatenated result
        return less_than + equal_to + greater_than