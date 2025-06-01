class Solution(object):
    def distributeCandies(self, n, limit):
        """
        :type n: int
        :type limit: int
        :rtype: int
        """

        # Helper function to calculate nCr (binomial coefficient) safely
        def nCr(n, r):
            if r > n or n < 0 or r < 0:
                return 0
            # Use a simple formula for nCr when r=2
            # C(n, 2) = n*(n-1)//2
            if r == 2:
                return n * (n - 1) // 2
            # For general cases (not needed here), can implement full factorial-based or iterative
            res = 1
            for i in range(r):
                res = res * (n - i) // (i + 1)
            return res

        # Step 1: Check feasibility
        if n > 3 * limit:
            return 0

        # Step 2: Calculate total ways without limits
        total_ways = nCr(n + 2, 2)

        # Step 3: Subtract ways where at least one child > limit
        one_child_exceed = 3 * nCr(n - limit + 1, 2)

        # Step 4: Add ways where at least two children > limit
        two_children_exceed = 3 * nCr(n - 2 * limit, 2)

        # Step 5: Subtract ways where all three children > limit
        three_children_exceed = nCr(n - 3 * limit - 1, 2)

        # Step 6: Apply inclusion-exclusion formula
        result = total_ways - one_child_exceed + two_children_exceed - three_children_exceed

        # Final step: return result, or 0 if negative
        return max(result, 0)
