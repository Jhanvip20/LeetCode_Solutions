class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:

            while l < r and not s[l].isalnum():  # Skip non-alphanumeric characters
                l += 1
            while l < r and not s[r].isalnum():  # Skip non-alphanumeric characters
                r -= 1
            
            if s[l].lower() != s[r].lower():  # Compare lowercase characters
                return False
            
            l += 1
            r -= 1
        
        return True