import math

class Solution:
    def create_high(self, num, st):
        high = 0
        mp1 = -1
        while st > 0:
            dig = num // st
            if mp1 == -1 and dig != 9:
                mp1 = dig
            if dig == mp1:
                high = high * 10 + 9
            else:
                high = high * 10 + dig
            num %= st
            st //= 10
        return high

    def create_low(self, num, st):
        low = 0
        mp1 = -1
        is_first_one = 0
        while st > 0:
            dig = num // st
            if is_first_one == 0:
                if dig == 1:
                    is_first_one = 1
                else:
                    is_first_one = -1
            if dig != 1 and mp1 == -1 and dig != 0:
                mp1 = dig
            if dig == mp1:
                low = low * 10 + (0 if is_first_one == 1 else 1)
            else:
                low = low * 10 + dig
            num %= st
            st //= 10
        return low

    def maxDiff(self, num: int) -> int:
        dig = int(math.log10(num)) + 1
        st = 10 ** (dig - 1)
        return self.create_high(num, st) - self.create_low(num, st)