from typing import List
from functools import lru_cache


class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        @lru_cache(None)
        def search(turn: int = 0,
                   mouse: int = 1,
                   cat: int = 2,
                   ):
            if turn == len(graph) * 2:
                return 0
            if mouse == cat:
                return 2
            if mouse == 0:
                return 1

            if (turn % 2) == 0:  # Mouse goes first
                if any(search(turn + 1, mouse_next, cat) == 1
                        for mouse_next in graph[mouse]):
                    return 1
                if all(search(turn + 1, mouse_next, cat) == 2
                        for mouse_next in graph[mouse]):
                    return 2
                return 0
            else:  # Cat's turn
                if any(search(turn + 1, mouse, cat_next) == 2
                        for cat_next in graph[cat] if cat_next != 0):
                    return 2
                if all(search(turn + 1, mouse, cat_next) == 1
                        for cat_next in graph[cat] if cat_next != 0):
                    return 1
                return 0

        return search()


sol = Solution()
print(sol.catMouseGame(
    graph=[[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]]))

print(sol.catMouseGame(
    graph=[[1, 3], [0], [3], [0, 2]]))
