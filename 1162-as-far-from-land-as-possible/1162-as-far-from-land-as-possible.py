class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        q = collections.deque()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        maxDistance = 0

        n = len(grid)

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i,j,0))
        
        if len(q) == n*n or len(q) == 0:
            return -1
        while q:
            r, c, dist = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    q.append((nr, nc, dist + 1))
                    grid[nr][nc] = 1
            maxDistance = max(maxDistance, dist)
        return maxDistance