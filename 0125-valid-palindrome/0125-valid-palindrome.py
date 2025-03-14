
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        t=""
        print(s)
        for i in s:
            if i.isalnum():
                t+=i.lower()
        print(t)
        return t==t[::-1]
        