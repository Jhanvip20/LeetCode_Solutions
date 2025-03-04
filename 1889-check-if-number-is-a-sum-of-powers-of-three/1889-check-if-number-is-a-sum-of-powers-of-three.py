class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            r = n % 3
            if r == 2:
                return False
            n //= 3  # Equivalent to n = n / 3,  to remove the last processed digit and repeat the process
        return True
        