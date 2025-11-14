class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1,0), (-1,0), (0,1), (0,-1)] 
        rowLen = len(grid)
        colLen = len(grid[0])
        q = collections.deque()
        fresh_count = 0
        res = 0
        for i in range(rowLen):
            for j in range(colLen):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    q.append((i,j, 0))
        
        if fresh_count == 0:
            return 0

        while q:
            r, c, minutes = q.popleft()
            res = max(res, minutes)
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rowLen and 0 <= nc < colLen and grid[nr][nc] == 1:
                    q.append((nr,nc, minutes + 1))
                    grid[nr][nc] = 2
                    fresh_count -= 1

        if fresh_count == 0:
            return res 
        else:
            return -1

        

