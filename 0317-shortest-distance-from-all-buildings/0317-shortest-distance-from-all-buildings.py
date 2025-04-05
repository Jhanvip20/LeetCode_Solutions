class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        buildings = {
            (i, j)
            for i, line in enumerate(grid)
            for j, elem in enumerate(line)
            if elem == 1
        }
        
        total_dist = Counter()
        cnt_buildings = Counter()

        def dfs(i, j, prev_number):
            q = deque()
            q.appendleft((i, j, 0))
            while q:
                x, y, d = q.pop()
                for u, v in ((x - 1, y), (x, y - 1),
                             (x + 1, y), (x, y + 1),):
                    if (
                        0 <= u < m and 0 <= v < n
                        and grid[u][v] == 0
                        and cnt_buildings[(u, v)] == prev_number
                    ):
                        q.appendleft((u, v, d + 1))
                        total_dist[(u, v)] += d + 1
                        cnt_buildings[(u, v)] += 1
        
        for prev_number, (i, j) in enumerate(buildings):
            dfs(i, j, prev_number)

        n_buildings = len(buildings)
        return min(
            (
                total_dist[k]
                for k, v in cnt_buildings.items()
                if v == n_buildings
            ),
            default=-1,
        )