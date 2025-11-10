class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rowLen = len(mat)
        colLen = len(mat[0])
        q = collections.deque()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        for i in range(rowLen):
            for j in range(colLen):
                if mat[i][j] == 0:
                    q.append((i, j, 0))
                else:
                    mat[i][j] = float("inf")
        
        while q:
            r, c, dist = q.popleft()

            if mat[r][c] > dist:
                mat[r][c] = dist
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rowLen and 0 <= nc < colLen:
                    if mat[nr][nc] == float("inf"):
                        q.append((nr, nc, dist + 1))
            
        return mat