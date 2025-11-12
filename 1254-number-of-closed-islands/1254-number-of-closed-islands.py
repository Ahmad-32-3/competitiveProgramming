class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()
        rowLen = len(grid)
        colLen = len(grid[0])
        res = 0

        def bfs(i,j) -> int:
            q.append((i,j))
            visited.add((i,j))
            isClosed = True

            while q:
                r, c = q.popleft()
                if r == 0 or r == rowLen - 1 or c == 0 or c == colLen - 1:
                    isClosed = False
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rowLen and 0 <= nc < colLen and grid[nr][nc] == 0 and ((nr, nc)) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))
            return isClosed
            
        
        for i in range(rowLen):
            for j in range(colLen):
                if grid[i][j] == 0 and ((i, j)) not in visited:
                    res += bfs(i,j)
        return res
