from typing import List

# from math import inf
from collections import deque


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:

        graph_size = len(graph)

        masks = [1 << i for i in range(graph_size)]
        all_visited = (1 << graph_size) - 1

        dq = deque([(i, masks[i]) for i in range(graph_size)])
        visited_states = [{masks[i]} for i in range(graph_size)]

        trip_count = 0

        while dq:

            n = len(dq)

            while n > 0:
                current_node, visited = dq.popleft()

                if visited == all_visited:
                    return trip_count

                for neighbor in graph[current_node]:
                    new_state = visited | masks[neighbor]

                    if new_state == all_visited:
                        return 1 + trip_count
                    if new_state not in visited_states[neighbor]:
                        visited_states[neighbor].add(new_state)
                        dq.append((neighbor, new_state))
                n -= 1

            trip_count += 1

        return -1


sol = Solution()
print(sol.shortestPathLength(graph=[[1, 2, 3], [0], [0], [0]]))
print(sol.shortestPathLength(graph=[[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]))
