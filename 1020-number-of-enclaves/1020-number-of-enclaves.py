class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()
        rowLen = len(grid)
        colLen = len(grid[0])
        res = 0

        def bfs(i,j) -> int:
            q.append((i,j))
            visited.add((i,j))
            counter = 0
            oak = False

            while q:
                r, c = q.popleft()
                if r == rowLen - 1 or r == 0 or c == colLen - 1 or c == 0:
                    oak = True
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rowLen and 0 <= nc < colLen and ((nr, nc)) not in visited and grid[nr][nc] == 1:
                        q.append((nr, nc))
                        visited.add((nr, nc))    
                if not oak:
                    counter += 1

            if not oak:
                return counter 
            else:
                return 0
                        

        for i in range(rowLen):
            for j in range(colLen):
                if grid[i][j] == 1 and ((i,j)) not in visited:
                    res += bfs(i,j)
        return res
                



