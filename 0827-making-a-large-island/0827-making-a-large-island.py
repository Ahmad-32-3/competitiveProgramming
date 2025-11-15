from collections import deque, defaultdict

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        island_id = 2  # start from 2 (since 0 = water, 1 = land)
        area = {}      # map island_id -> island size

        # --- BFS to label each island and count its size ---
        def bfs(r, c, id):
            q = deque([(r, c)])
            grid[r][c] = id
            size = 1

            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = id
                        size += 1
                        q.append((nx, ny))
            return size

        # 1️ Label all existing islands
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    area[island_id] = bfs(i, j, island_id)
                    island_id += 1

        # If all land already
        if not area:
            return 1  # all zeros, flip one
        max_area = max(area.values())
        if max_area == n * n:
            return max_area

        # 2️ Try flipping one 0 and see how many unique islands it connects
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = set()
                    total = 1  # flipping this cell
                    for dx, dy in directions:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] > 1:
                            id = grid[nx][ny]
                            if id not in seen:
                                seen.add(id)
                                total += area[id]
                    max_area = max(max_area, total)

        return max_area
