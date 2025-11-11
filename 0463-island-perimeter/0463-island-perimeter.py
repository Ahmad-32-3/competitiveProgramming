class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rowLen = len(grid)
        colLen = len(grid[0])
        q = collections.deque()
        found = False
        res = 0
        visited = set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        for i in range(rowLen):
            for j in range(colLen):
                if grid[i][j] == 1:
                    q.append((i,j))
                    found = True
                    break
            if found:
                break
        
        while q:
            r, c = q.popleft()
            visited.add((r,c))
            perimeter = 4

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rowLen and 0 <= nc < colLen:
                    if grid[nr][nc] == 1:
                        perimeter -= 1

                        if ((nr, nc)) not in visited:
                            q.append((nr, nc))
                            visited.add((nr, nc))
            res += perimeter

        return res




                    
        
