class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rowLen = len(board)
        colLen = len(board[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        q = collections.deque()
        res = 0
        visited = set()
        def bfs(i,j):
            q.append((i,j))
            visited.add((i,j))
            
            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rowLen and 0 <= nc < colLen:
                        if ((nr, nc)) not in visited and board[nr][nc] == 'X':
                            q.append((nr, nc))
                            visited.add((nr, nc))
        for i in range(rowLen):
            for j in range(colLen):
                if board[i][j] == 'X':
                    if ((i, j)) not in visited:
                        bfs(i, j)
                        res += 1
        return res
        









