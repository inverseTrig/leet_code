from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces_count = 0
        visited = set()

        def dfs(n: int):
            for island_index, connected in enumerate(isConnected[n]):
                if connected and island_index not in visited:
                    visited.add(island_index)
                    dfs(island_index)

        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                provinces_count += 1
        return provinces_count

sol = Solution()
print(sol.findCircleNum(isConnected = [[1,1,0],[1,1,0],[0,0,1]]))
