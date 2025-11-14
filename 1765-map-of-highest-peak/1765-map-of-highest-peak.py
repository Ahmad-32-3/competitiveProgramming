class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rowLen = len(isWater)
        colLen = len(isWater[0])

        q = collections.deque()
        visited = set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        land = 0

        for i in range(rowLen):
            for j in range(colLen):
                if isWater[i][j] == 1:
                    q.append((i,j))
                    visited.add((i,j))
                    isWater[i][j] = 0
                else:
                    land += 1
        height = 0
        while q and land:
            height += 1
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rowLen and 0 <= nc < colLen and ((nr, nc)) not in visited:
                        isWater[nr][nc] = height
                        land -= 1
                        visited.add((nr,nc))
                        q.append((nr, nc))
        return isWater
                        