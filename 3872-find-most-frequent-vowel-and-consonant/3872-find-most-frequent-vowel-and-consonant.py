class Solution:
    def maxFreqSum(self, s: str) -> int:
        return max(list(Counter(i for i in s if i not in 'aeiou').values())+[0]) + max(list(Counter(i for i in s if i in 'aeiou').values())+[0])
        