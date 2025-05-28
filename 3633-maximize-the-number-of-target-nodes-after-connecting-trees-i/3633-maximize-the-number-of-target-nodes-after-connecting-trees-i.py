from collections import deque

class Solution:
    def maxTargetNodes(self, edges1, edges2, k):
        def bfs(start, adj, k):
            if k == 0:
                return 1
            visited = set([start])
            q = deque([start])
            level = 0
            nodes_reached = 1

            while q and level < k:
                for _ in range(len(q)):
                    node = q.popleft()
                    for neighbor in adj[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)
                            nodes_reached += 1
                level += 1
            return nodes_reached

        n = max(max(e) for e in edges1) + 1
        m = max(max(e) for e in edges2) + 1

        adj1 = [[] for _ in range(n)]
        adj2 = [[] for _ in range(m)]

        for u, v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)

        for u, v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)

        path1 = [bfs(i, adj1, k) for i in range(n)]

        max_found = 0
        if k > 0:
            for i in range(m):
                max_found = max(max_found, bfs(i, adj2, k - 1))

        return [p + max_found for p in path1]
        