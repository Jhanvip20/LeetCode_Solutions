class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip() # Ignore Leading Whitespace
        if not s: #check for empty string
            return 0
        
        sign, index, result = 1, 0, 0         # Initialize sign as positive (1) and start index and result
        if s[index] in '+-':    #Check for a sign ('+' or '-') at the beginning
            sign = -1 if s[index] == '-' else 1
            index += 1
        #Process digits in the string
        while index < len(s) and s[index].isdigit():
            result = result * 10 + int(s[index])
            index += 1
            #Handle overflow/underflow within 32-bit integer range
            if sign * result > (2**31 - 1):
                return 2**31 - 1 
            if sign * result <= -2**31:
                return -2**31
               
        return result * sign #Return the final result with the correct sign

        

        