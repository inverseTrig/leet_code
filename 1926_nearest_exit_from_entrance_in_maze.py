from typing import List
from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        nei = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        dq, seen = deque(), set()
        dq.append(entrance)

        row, col = len(maze), len(maze[0])

        steps = 0
        while dq:
            n = len(dq)
            for _ in range(n):
                i, j = dq.popleft()
                # print(f'popped: {i}, {j}')
                if (i, j) in seen:
                    continue

                seen.add((i, j))
                if (i == 0 or i == row - 1
                        or j == 0 or j == col - 1) \
                        and [i, j] != entrance:

                    return steps

                for di, dj in nei:
                    new_i, new_j = i + di, j + dj
                    if 0 <= new_i < row \
                            and 0 <= new_j < col \
                            and maze[new_i][new_j] == '.':
                        dq.append((new_i, new_j))

            steps += 1

        return -1


sol = Solution()
# print(sol.nearestExit(maze=[["+", "+", ".", "+"],
#                             [".", ".", ".", "+"],
#                             ["+", "+", "+", "."]],
#                       entrance=[1, 2],
#                       ))
# print(sol.nearestExit(maze=[["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]],
#                       entrance=[1, 0],
#                       ))


# print(sol.nearestExit(maze=[["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]],
#                       entrance=[1, 2],
#                       ))
