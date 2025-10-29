class Solution:
    def validSubarraySplit(self, nums: List[int]) -> int:
        def backtrack(start):
            if start in vis: # Check memory
                return vis[start] 
            ans = float('inf')
            for i in range(L-1,start-1,-1):
                if gcd(nums[i],nums[start]) != 1: 
                    ans = min(ans, 1+backtrack(i+1))
            vis[start] = ans # Memorize
            return ans
        
        L = len(nums)
        vis = {L:0} # Initialize memory
        return backtrack(0) if backtrack(0) != float('inf') else -1