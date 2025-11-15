class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        pacificQueue = collections.deque()
        atlanticQueue = collections.deque()
        pacificSet = set()
        atlanticSet = set()
        rowLen = len(heights)
        colLen = len(heights[0])
        res = []
        for i in range(rowLen):
            pacificQueue.append((i, 0))
            pacificSet.add((i, 0))
            atlanticQueue.append((i, colLen - 1))
            atlanticSet.add((i, colLen - 1))

        for j in range(colLen):
            pacificQueue.append((0, j))
            pacificSet.add((0, j))
            atlanticQueue.append((rowLen - 1, j))
            atlanticSet.add((rowLen - 1, j))

        while pacificQueue:
            r, c = pacificQueue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rowLen and 0 <= nc < colLen and heights[nr][nc] >= heights[r][c] and ((nr, nc)) not in pacificSet:
                    pacificQueue.append((nr ,nc))
                    pacificSet.add((nr, nc))
        while atlanticQueue:
            r, c = atlanticQueue.popleft()


            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rowLen and 0 <= nc < colLen and heights[nr][nc] >= heights[r][c] and ((nr,nc)) not in atlanticSet:
                    atlanticQueue.append((nr ,nc))
                    atlanticSet.add((nr, nc))
            
        for r in range(rowLen):
            for c in range(colLen):
                if (r, c) in pacificSet and (r, c) in atlanticSet:
                    res.append([r, c])

        return res