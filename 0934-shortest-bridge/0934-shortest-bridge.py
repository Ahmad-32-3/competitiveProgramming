class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        size = len(grid)
        def bfs(i,j):
            q = collections.deque()
            q.append((i,j))
            while q:
                r, c = q.popleft()
                grid[r][c] = 2
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < size and 0 <= nc < size and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr,nc))
        flag = False
        for i in range(size):
            if flag:
                break
            for j in range(size):
                if grid[i][j] == 1:
                    bfs(i,j)
                    flag = True
                    break
        q = collections.deque()
        visited = set()
        for i in range(size):
            for j in range(size):
                if grid[i][j] == 2:
                    for dr, dc in directions:
                        nr, nc = i + dr, j + dc
                        if 0 <= nr < size and 0 <= nc < size and grid[nr][nc] == 0 and ((nr, nc)) not in visited:
                            q.append((nr,nc,1))
                            visited.add((nr,nc))
        while q:
            r, c, dist = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < size and 0 <= nc < size and ((nr, nc)) not in visited:
                    if grid[nr][nc] == 0:
                        q.append((nr, nc, dist + 1))
                        visited.add((nr,nc))
                    elif grid[nr][nc] == 1:
                        return dist
      
        