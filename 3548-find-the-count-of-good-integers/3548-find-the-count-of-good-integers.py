from collections import Counter
from math import factorial

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        # 1. Generate all possible n‑digit palindromes
        palindromes = []
        half = (n + 1) // 2
        start = 10 ** (half - 1)
        end = 10**half
        for half_part in range(start, end):
            half_str = str(half_part)
            full_str = half_str + half_str[-2::-1] if n % 2 else half_str + half_str[::-1]
            palindromes.append(int(full_str))

        # 2. Filter palindromes divisible by k
        divisible = [str(num) for num in palindromes if num % k == 0]

        # 3. Remove duplicates by digit composition
        unique_nums = set()
        for num_str in divisible:
            s = "".join(sorted(list(num_str)))
            if s in unique_nums:
                continue
            unique_nums.add(s)

        answer = 0
        for num_str in list(unique_nums):
            counter = Counter(num_str)

            # 4. Count total permutations of digits
            total = factorial(len(num_str))
            for val in counter.values():
                total //= factorial(val)
            answer += total

            # 5. Remove permutations that have leading zero
            if "0" in num_str:
                counter["0"] -= 1
                total_with_leading_zero = factorial(len(num_str) - 1)
                for val in counter.values():
                    total_with_leading_zero //= factorial(val)
                answer -= total_with_leading_zero

        return answer
        