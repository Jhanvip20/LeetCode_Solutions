class Solution:
    def assignBikes(self, workers, bikes):
        n, m, dp = len(workers), len(bikes), {}

        def mdist(a,b):
            return abs(a[0]-b[0]) + abs(a[1]-b[1])

        def backtrack(i,visited):
            if i == n:
                return 0 

            if tuple(visited) in dp:
                return dp[tuple(visited)]

            min_val = float("inf")

            for j in range(m):
                if visited[j] == True: continue
                visited[j] = True
                min_val = min(min_val,mdist(workers[i],bikes[j])+backtrack(i+1,visited))
                visited[j] = False

            dp[tuple(visited)] = min_val 

            return dp[tuple(visited)]

        visited = [False]*m

        return backtrack(0,visited)





        
        
        
        