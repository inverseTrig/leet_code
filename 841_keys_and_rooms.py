from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        keys = [0]

        while keys:
            key = keys.pop()
            if key in visited:
                continue

            keys.extend(rooms[key])
            if key not in visited:
                visited.add(key)

        return len(visited) == len(rooms)


sol = Solution()
print(sol.canVisitAllRooms(rooms=[[1], [2], [3], []]))
print(sol.canVisitAllRooms(rooms=[[1, 3], [3, 0, 1], [2], [0]]))
