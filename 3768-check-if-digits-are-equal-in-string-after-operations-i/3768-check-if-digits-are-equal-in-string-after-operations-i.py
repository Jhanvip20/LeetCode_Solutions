class Solution:
    def hasSameDigits(self, s: str) -> bool:
        return eq(*reduce(lambda q,_:[sum(p)%10 for p in pairwise(q)],s[2:],map(int,s)))