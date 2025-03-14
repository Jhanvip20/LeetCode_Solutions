class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sub_num = {0:1} # Initialize the dictionary with 0:1, as there is one way to get a cumulative sum of 0 (initially)
        total = count = 0

        for n in nums:
            total += n # Update cumulative sum
            # If (current cumulative sum - k) exists in the dictionary, add its count to the result
            if total - k in sub_num:
                count += sub_num[total-k]
            
            # Update the dictionary with the current cumulative sum
            if total in sub_num:
                sub_num[total] += 1
            else:
                sub_num[total] = 1
            
            # OR -- sub_num[total] = 1 + sub_num.get(total, 0)
        
        return count