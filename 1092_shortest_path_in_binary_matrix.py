from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        N = len(grid)
        visited = set()
        nei = [(-1, -1), (-1, 0), (-1, 1),
               (0, -1), (0, 1),
               (1, -1), (1, 0), (1, 1)]

        queue = deque([(1, 0, 0)])
        while queue:
            distance, x, y = queue.popleft()
            if x == y == N - 1:
                return distance

            for dx, dy in nei:
                if 0 <= x + dx < N \
                        and 0 <= y + dy < N \
                        and grid[x + dx][y + dy] == 0 \
                        and (x + dx, y + dy) not in visited:
                    visited.add((x + dx, y + dy))
                    queue.append((distance + 1, x + dx, y + dy))
        return -1
