
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1, -1)]
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        q = collections.deque()
        visited = set()
        q.append((0, 0, 0))
        visited.add((0,0))

        while q:
            r, c, path = q.popleft()

            if r == n - 1 and c == n - 1:
                return path + 1

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and ((nr, nc)) not in visited and grid[nr][nc] == 0:
                    q.append((nr, nc, path + 1))
                    visited.add((nr, nc))
        return -1
