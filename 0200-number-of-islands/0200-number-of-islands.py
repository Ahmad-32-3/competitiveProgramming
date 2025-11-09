class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        # down, up, right, left
        island = 0
        visited = set()

        def bfs (r, c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r, c))

            while q:
                r, c = q.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):

                        if grid[nr][nc] == "1" and ((nr, nc)) not in visited:
                            q.append((nr, nc))
                            visited.add((nr,nc))


        for i in range(len(grid)):
            for j in range (len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i,j)
                    island += 1
        return island
