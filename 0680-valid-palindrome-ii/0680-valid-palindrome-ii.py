class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0 # pointer one
        right = len(s) - 1 # pointer two
        
        while left < right: # index should be less then right one, not even equal, as  we dont need to compare same index
            if s[left] == s[right]: # if both the ends value are equal.
                left += 1 # if yes increase them both
                right -= 1
            else: # if not, we will check if it is after removing either right of left value
                return s[left:right] == s[left:right][::-1] or s[left+1:right+1] == s[left+1:right+1][::-1] # return true if either situation is True.
        
        return True # True as both ends values are same.
        