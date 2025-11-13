class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        q = collections.deque()
        visited = set()
        rowLen = len(grid)
        colLen = len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        q.append((row, col))
        visited.add((row, col))
        val = grid[row][col]
        arr = []

        while q:
            r, c = q.popleft()
            counter = 4
            

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rowLen and 0 <= nc < colLen and grid[nr][nc] == val:
                    counter -= 1
                    if ((nr, nc)) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))
                    
                
            if r == 0 or r == rowLen - 1 or c == 0 or c == colLen - 1 or counter != 0:
                arr.append((r,c))

        for r, c in arr:
            grid[r][c] = color

        return grid
        
        
                    

