class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        from collections import deque
        
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def bfs(i, j):
            q = deque([(i, j)])
            grid[i][j] = 0  # mark visited
            count = 1
            touches_border = (i == 0 or j == 0 or i == rows-1 or j == cols-1)
            
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        q.append((nr, nc))
                        count += 1
                        if nr == 0 or nr == rows-1 or nc == 0 or nc == cols-1:
                            touches_border = True
            return 0 if touches_border else count
        
        enclaves = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    enclaves += bfs(i, j)
        return enclaves
