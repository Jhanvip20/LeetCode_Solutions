class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:

        diffs = [b - a for a, b in zip(stations, stations[1:])]
        count = lambda x: sum(d//x for d in diffs)

        left, right = 0.000001, max(diffs)

        while right - left > 0.000001:
            mid = (left + right) / 2

            if count(mid) > k: left  = mid
            else             : right = mid

        return left