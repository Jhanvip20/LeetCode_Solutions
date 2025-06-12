class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        current = 1
        k -= 1
        
        while k > 0:
            count = self.countSteps(n, current, current + 1)
            if count <= k:
                current += 1
                k -= count
            else:
                current *= 10
                k -= 1
        
        return current

    def countSteps(self, n: int, curr: int, next: int) -> int:
        steps = 0
        while curr <= n:
            steps += min(n + 1, next) - curr
            curr *= 10
            next *= 10
        return steps