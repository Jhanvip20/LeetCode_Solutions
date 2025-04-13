class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        even_count = (n + 1) // 2
        odd_count = n // 2
        return (pow(5, even_count, mod) * pow(4, odd_count, mod)) % mod