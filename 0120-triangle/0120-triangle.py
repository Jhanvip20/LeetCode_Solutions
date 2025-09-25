class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):  # for each row in triangle (skipping the first),
            for j in range(i+1):           # loop through each element in the row
                triangle[i][j] += min(triangle[i-1][j-(j==i)],  # minimum sum from coordinate (x-1, y)
                                      triangle[i-1][j-(j>0)])   # minimum sum from coordinate (x-1, y-1)
        return min(triangle[-1])  # obtain minimum sum from last row