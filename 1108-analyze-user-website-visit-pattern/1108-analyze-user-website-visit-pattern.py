class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        from itertools import combinations, permutations
        user_traj = defaultdict(SortedList)
        for u,t,w in zip(username, timestamp, website):
            user_traj[u].add((t,w))
        traj_counts = defaultdict(int)
        for u in user_traj:
            order_w = [w for _, w in user_traj[u]]
            seen_patterns = set()
            for p in combinations(order_w, 3):
                seen_patterns.add(p)
            for pat in seen_patterns:
                traj_counts[pat] += 1

        max_v = max(traj_counts.values())
        cands = SortedList()
        for k in traj_counts:
            if traj_counts[k] == max_v:
                cands.add(k)
        return cands[0]