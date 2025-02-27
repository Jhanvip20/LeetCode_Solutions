class Solution:
    def isPalindrome(self, x: int) -> bool:
        original_num = x

        #Negative numbers and number ending in 0 are not palindrome
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reverse = 0
        while x > 0:
            digit = x % 10
            x //= 10 # BE CAREFUL - Here x value is going to change so store x value in original num at beginnimg
            reverse = reverse * 10 + digit

        if original_num == reverse:
            return True
        else:
            return False

        