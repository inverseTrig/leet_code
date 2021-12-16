class Solution:
    def countPoints(self, rings: str) -> int:
        mask = {'R': 1,
                'G': 2,
                'B': 4}
        rods = [0] * 10

        for i in range(0, len(rings), 2):
            color, rod = rings[i], int(rings[i + 1])
            rods[rod] |= mask[color]

        return rods.count(7)


sol = Solution()
print(sol.countPoints(rings="B0B6G0R6R0R6G9"))
print(sol.countPoints(rings="B0R0G0R9R0B0G0"))
print(sol.countPoints(rings="G4"))
