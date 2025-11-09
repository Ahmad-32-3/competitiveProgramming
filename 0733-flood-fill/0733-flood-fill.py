class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # down, up, right, left
        queue = collections.deque()
        visited = set()

        queue.append((sr, sc))
        visited.add((sr, sc))

        start_colour = image[sr][sc]

        while queue:
            r, c = queue.popleft()
            image[r][c] = color

            for dr, dc in directions:
                nr, nc = (r + dr, c + dc)

                if 0 <= nr < len(image) and 0 <= nc < len(image[0]):

                    if (nr, nc) not in visited and image[nr][nc] == start_colour:
                        queue.append((nr, nc))
                        visited.add((nr, nc))
        return image

