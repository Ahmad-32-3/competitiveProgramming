class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        rowLen = len(grid)
        colLen = len(grid[0])
        res = 0
        def bfs(r,c) -> int:
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            tot = 0

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rowLen and 0 <= nc < colLen:
                        if (nr, nc) not in visited and grid[nr][nc] == 1:
                            q.append((nr, nc))
                            visited.add((nr, nc))
                tot += 1

            return tot
        
        for i in range(rowLen):
            for j in range(colLen):
                if grid[i][j] == 1 and (i,j) not in visited:
                    res = max(res, bfs(i,j))
        return res



