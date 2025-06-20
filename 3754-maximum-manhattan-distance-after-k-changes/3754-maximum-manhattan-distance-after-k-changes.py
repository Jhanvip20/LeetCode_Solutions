class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        x, y = 0, 0
        dist = []
        for i in s:
            if i == 'N':
                y += 1
            elif i == 'W':
                x -= 1
            elif i == 'E':
                x += 1
            else:
                y -= 1
            dist.append((abs(x) + abs(y)))
        n = len(dist)
        i = 1
        count = 0
        maxDist = dist[1]
        prev = dist[0]
        if k == 0:
            return max(dist)
        while (i < n):
            if dist[i] < prev and k > 0:
                count += 2
                k -= 1
            prev = dist[i]
            dist[i] += count
            maxDist = max(maxDist, dist[i])
            i += 1
        return maxDist
