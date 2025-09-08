import heapq

class Solution:
    def maxAverageRatio(self, classes, extraStudents):
        # Max heap: store (-gain, index)
        pq = []
        for i, (p, t) in enumerate(classes):
            curr = p / t
            newPr = (p + 1) / (t + 1)
            heapq.heappush(pq, (-(newPr - curr), i))

        # Distribute extra students
        while extraStudents > 0:
            gain, i = heapq.heappop(pq)
            p, t = classes[i]
            classes[i][0] += 1
            classes[i][1] += 1
            curr = classes[i][0] / classes[i][1]
            newPr = (classes[i][0] + 1) / (classes[i][1] + 1)
            heapq.heappush(pq, (-(newPr - curr), i))
            extraStudents -= 1

        # Compute final average pass ratio
        ans = sum(p / t for p, t in classes)
        return ans / len(classes)