MOD = 10**9 + 7

class Solution:
    def numTilings(self, n: int) -> int:
        # Handle base cases
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5
        
        # DP array to store number of ways to tile a 2 x n board
        dp = [0] * (n + 1)
        prefix = [0] * (n + 1)
        
        # Initialize base cases
        dp[0] = 1  # 1 way to tile a 2 x 0 board
        dp[1] = 1  # 1 way to tile a 2 x 1 board
        dp[2] = 2  # 2 ways to tile a 2 x 2 board
        dp[3] = 5  # 5 ways to tile a 2 x 3 board
        
        prefix[0] = dp[0]
        prefix[1] = prefix[0] + dp[1]
        prefix[2] = prefix[1] + dp[2]
        prefix[3] = prefix[2] + dp[3]
        
        # Fill dp array using the correct recurrence relation
        for i in range(4, n + 1):
            dp[i] = (dp[i-1] + dp[i-2] + 2 * prefix[i-3]) % MOD
            prefix[i] = (prefix[i-1] + dp[i]) % MOD
        
        return dp[n]

sol = Solution()
print(sol.numTilings(3))  # Output: 5
print(sol.numTilings(4))  # Output: 11
