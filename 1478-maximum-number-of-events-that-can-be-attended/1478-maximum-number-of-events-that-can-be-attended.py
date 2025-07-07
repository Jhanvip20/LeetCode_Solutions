from heapq import heappush, heappop
from typing import List

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        total = max(event[1] for event in events)

        pq = []  # Min-heap of end days
        i = 0
        day, cnt = 1, 0

        while day <= total:
            if not pq and i < len(events):
                day = max(day, events[i][0])

            # Remove past events
            while pq and pq[0] < day:
                heappop(pq)

            # Add events starting today
            while i < len(events) and events[i][0] == day:
                heappush(pq, events[i][1])
                i += 1

            # Attend the event that ends earliest
            if pq:
                heappop(pq)
                cnt += 1
            elif i == len(events):  # No more events to process
                break

            day += 1

        return cnt