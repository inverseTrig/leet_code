from typing import List


class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        water_spent = 0
        for i, p in enumerate(plants):
            # If should have refilled from last step
            if water_spent + p > capacity:
                steps += 2 * (i + 1) - 1
                water_spent = p
            else:
                steps += 1
                water_spent += p
        return steps


sol = Solution()
print(sol.wateringPlants(plants=[2, 2, 3, 3], capacity=5))
print(sol.wateringPlants(plants=[1, 1, 1, 4, 2, 3], capacity=4))
print(sol.wateringPlants([7, 7, 7, 7, 7, 7, 7], capacity=8))
