class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip() # Ignore Leading Whitespace
        if not s:
            return 0
        
        sign, index, result = 1, 0, 0
        if s[index] in '+-':
            sign = -1 if s[index] == '-' else 1
            index += 1
        
        while index < len(s) and s[index].isdigit():
            result = result * 10 + int(s[index])
            index += 1

            if sign * result > (2**31 - 1):
                return 2**31 - 1 
            if sign * result <= -2**31:
                return -2**31
               
        return result * sign

        

        