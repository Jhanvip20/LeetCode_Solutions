class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int):
        l, count = 0, 0
        d = defaultdict(int)
        
        for r in range(len(S)):
            d[S[r]] += 1
            while d[S[r]] > 1:
                d[S[l]] -= 1
                l += 1
            if r - l + 1 == K:
                d[S[l]] -= 1
                l += 1
                count += 1

        return count
		
        