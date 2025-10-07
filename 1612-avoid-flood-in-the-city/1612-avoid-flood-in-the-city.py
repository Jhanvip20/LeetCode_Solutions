class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        last = {}
        q = deque()
        res = []
        for i, lake in enumerate(rains):
            if lake:
                if lake in last:
                    for j in q:
                        if j > last[lake]:
                            res[j] = lake
                            q.remove(j)
                            break
                    else:
                        return []
                res.append(-1)
                last[lake] = i
            else:
                res.append(1)
                q.append(i)
        return res 