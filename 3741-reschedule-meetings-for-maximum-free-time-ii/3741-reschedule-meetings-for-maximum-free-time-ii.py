class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        gap = [0] * (n + 1)
        lastEnd = 0
        for i in range(n):
            gap[i] = startTime[i] - lastEnd
            lastEnd = endTime[i]
        
        gap[n] = eventTime - lastEnd
        rightMax = [0] * (n + 1)
        for i in range(n - 1, - 1, -1):
            rightMax[i] = max(rightMax[i + 1], gap[i + 1])
        
        leftMax = 0
        maxGap = 0
        for i in range(1, n + 1):
            dur = endTime[i - 1] - startTime[i - 1]
            gapL = gap[i - 1]
            gapR = gap[i]

            if leftMax >= dur or rightMax[i] >= dur:
                maxGap = max(maxGap, gapL + dur + gapR)
            maxGap = max(maxGap, gapL + gapR)
            leftMax = max(leftMax, gapL)
        return maxGap