from typing import List
import heapq


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        rows, cols = len(heightMap), len(heightMap[0])
        water = 0
        q = []

        for r in range(rows):
            heapq.heappush(q, (heightMap[r][0], r, 0))
            heapq.heappush(q, (heightMap[r][cols - 1], r, cols - 1))

        for c in range(1, cols - 1):
            heapq.heappush(q, (heightMap[0][c], 0, c))
            heapq.heappush(q, (heightMap[rows - 1][c], rows - 1, c))

        visited = {(r, c) for _, r, c in q}

        while q:

            h, r, c = heapq.heappop(q)

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                r1, c1 = r + dr, c + dc
                if (r1, c1) not in visited and r1 >= 0 \
                        and c1 >= 0 and r1 < rows and c1 < cols:
                    visited.add((r1, c1))
                    water += max(0, h - heightMap[r1][c1])
                    heapq.heappush(q, (max(h, heightMap[r1][c1]), r1, c1))

        return water
