MODULO = int(1e9 + 7)
MAX_VALUE = 10_000

STRICT_COUNTS = [[i + 1 for i in range(MAX_VALUE)]]
prev_row = [1] * MAX_VALUE
next_row = [0] * MAX_VALUE
prev_base = 1

while (prev_base << 1) <= MAX_VALUE:
    next_base = prev_base << 1
    for i in range(next_base - 1, MAX_VALUE):
        next_row[i] = 0
    for prev_num in range(prev_base, MAX_VALUE + 1):
        prev_count = prev_row[prev_num - 1]
        for mult in range(2, MAX_VALUE + 1):
            product = prev_num * mult
            if product > MAX_VALUE:
                break
            next_row[product - 1] = (next_row[product - 1] + prev_count) % MODULO
    current_counts = [next_row[next_base - 1]]
    for next_num in range(next_base, MAX_VALUE):
        current_counts.append((current_counts[-1] + next_row[next_num]) % MODULO)
    STRICT_COUNTS.append(current_counts)
    prev_base = next_base
    prev_row, next_row = next_row, prev_row

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        count = 0
        combo = 1
        top = n - 1
        bottom = 1
        base = 1
        for k in range(min(n, len(STRICT_COUNTS))):
            if base <= maxValue:
                count = (count + combo * STRICT_COUNTS[k][maxValue - base]) % MODULO
            else:
                break
            combo = combo * top // bottom
            top -= 1
            bottom += 1
            base <<= 1
        return count