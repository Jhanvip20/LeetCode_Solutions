class Solution:
    def makeFancyString(self, s: str) -> str:
        p1 = 0
        cur = 1
        fancyString = s[0]
        
        for i in range(1, len(s)):
            if s[i] == s[p1]:
                cur += 1
            else:
                cur = 1
                p1 = i
            
            if cur > 2:
                continue
            fancyString += s[i]
        
        return fancyString