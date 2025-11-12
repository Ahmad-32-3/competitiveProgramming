class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = collections.deque()
        visited = set()

        q.append(start)
        visited.add(start)
        size = len(arr)

        while q:
            i = q.popleft()
            if arr[i] == 0:
                return True
            
            directions = [(arr[i]), (- arr[i])]

            for d in directions:
                new = i + d

                if 0 <= new < size and new not in visited:
                    q.append(new)
                    visited.add(new)
        return False
