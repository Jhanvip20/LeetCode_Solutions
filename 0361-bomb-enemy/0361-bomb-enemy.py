class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        colHits = [-1] * n
        ans = 0
        for i in range(m):
            j = 0
            while j < n:
                rowHits = 0
                while j < n and grid[i][j] != 'W':
                    if grid[i][j] == 'E':
                        rowHits += 1
                    j += 1
                if j < n:
                    colHits[j] = - 1
                k = j - 1
                while k >= 0 and grid[i][k] != 'W':
                    if grid[i][k] == '0':
                        if colHits[k] != -1:
                            ans = max(ans, rowHits + colHits[k])
                        else:
                            p = i + 1
                            colHits[k] = 0
                            while p < m and grid[p][k] != 'W':
                                if grid[p][k] == 'E':
                                    colHits[k] += 1
                                p += 1

                            p = i - 1 
                            while p >= 0 and grid[p][k] != 'W':
                                if grid[p][k] == 'E':
                                    colHits[k] += 1
                                p -= 1
                            ans = max(ans, rowHits + colHits[k])
                    k -= 1
                j += 1
        return ans
                