from typing import List
from collections import defaultdict


class Solution:
    def calcEquation(self,
                     equations: List[List[str]],
                     values: List[float],
                     queries: List[List[str]],
                     ) -> List[float]:
        mapping = defaultdict(dict)
        for (x, y), v in zip(equations, values):
            mapping[x][y] = v
            mapping[y][x] = 1 / v
        # print(mapping)

        def bfs(src, dst):
            if not (src in mapping and src in mapping):
                return -1.0
            todo, seen = [(src, 1.0)], set()
            for x, val in todo:
                if x == dst:
                    return val
                seen.add(x)
                for y in mapping[x]:
                    if y not in seen:
                        todo.append((y, val * mapping[x][y]))
            return -1.0

        return [bfs(src, dst) for src, dst in queries]


sol = Solution()
print(sol.calcEquation(equations=[["a", "b"], ["b", "c"]],
                       values=[2.0, 3.0],
                       queries=[["a", "c"],
                                ["b", "a"],
                                ["a", "e"],
                                ["a", "a"],
                                ["x", "x"],
                                ]))
