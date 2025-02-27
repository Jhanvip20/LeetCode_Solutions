class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        sign = -1 if x < 0 else 1
        x = abs(x) #absolute value

        # reversed_x = int(str(x)[::-1]) #convert into str and reverse, then convert back to int

        while x:
            digit = x % 10 # Extract Last digit
            x //= 10 # Remove the last digit from x
            result = result * 10 + digit # Append digit to the result
        result *=sign #Restore original sign

        #check for 32-bit integer overflow
        if result <-2**31 or result > 2**31 - 1:
            return 0
        
        return result
        