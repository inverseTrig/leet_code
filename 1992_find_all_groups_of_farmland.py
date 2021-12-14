from typing import List


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def clear_farmland(i: int, j: int) -> List[int]:
            di, dj = 0, 0
            while i + di < len(land) and land[i + di][j] == 1:
                di += 1
            while j + dj < len(land[0]) and land[i][j + dj] == 1:
                dj += 1

            for _i in range(i, i + di):
                for _j in range(j, j + dj):
                    land[_i][_j] = 0

            # print(f'land: {land}')

            return [i, j, i + di - 1, j + dj - 1]

        all_farmland = []
        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] == 1:
                    farmland = clear_farmland(i, j)
                    all_farmland.append(farmland)

        return all_farmland


sol = Solution()
# print(sol.findFarmland(land=[[1, 0, 0], [0, 1, 1], [0, 1, 1]]))
print(sol.findFarmland(land=[[1, 1, 1], [0, 0, 0], [0, 1, 1]]))
# print(sol.findFarmland(land=[[1, 1], [1, 1]]))
# print(sol.findFarmland(land=[[0]]))
