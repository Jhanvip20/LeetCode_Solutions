class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}                 #dictionary (memo) stores previously computed results to avoid redundant calculations.

        def dp(i: int, j: int) -> bool:            # recursive fun
            if (i, j) in memo:
                return memo[(i, j)]
            
            if j == len(p):    #If we reach the end of p, the result is True only if we also reached the end of s.
                return i == len(s)
            # This checks if the current character of s matches p:
                # Case 1: Exact character match (s[i] == p[j])
                # Case 2: . wildcard matches any character (p[j] == '.')
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

            # If the next character in p is *, we have two choices:
                # 1.Skip this char* combination (dp(i, j+2))
                # 2. Use char* and move to the next character in s (first_match and dp(i+1, j))

            if j + 1 < len(p) and p[j+1] == '*':
                ans = dp(i, j+2) or (first_match and dp(i+1, j))     
                # dp(i, j+2) → Ignore the char* pattern (treat * as zero occurrences).
                # first_match and dp(i+1, j) → Use char* and check the next character in s.                                 
            else:
                ans = first_match and dp(i+1, j+1) # If there's no *, we simply move both i and j forward if s[i] matches p[j].
            
            memo[(i, j)] = ans #cache the result to optimize performance (avoid redundant calculations).
            return ans
        
        return dp(0, 0) # Initial call to dp(0, 0) to check the full strings.
        
         
        