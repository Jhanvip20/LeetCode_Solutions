class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def f(n):
            return 0 if n < 0 else (n + 1) * (n + 2) // 2

        return f(n) - 3 * f(n - (limit + 1)) + 3 * f(n - 2 * (limit + 1)) - f(n - 3 * (limit + 1))
        