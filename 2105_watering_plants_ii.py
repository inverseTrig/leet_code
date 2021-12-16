from typing import List


class Solution:
    def minimumRefill(self,
                      plants: List[int],
                      capacityA: int,
                      capacityB: int) -> int:
        N = len(plants)
        refills = 0
        alice, bob = capacityA, capacityB

        def water(who, capacity, amount):
            nonlocal refills
            if who < amount:
                # print(f'refilling...')
                refills += 1
                who = capacity - amount
            else:
                who -= amount
            return who

        for i in range((N + 1) // 2):
            if i == N - i - 1:
                if bob > alice:
                    # print(f'bob is watering i: {i}')
                    bob = water(bob, capacityB, plants[i])
                else:
                    # print(f'alice is watering i: {i}')
                    alice = water(alice, capacityA, plants[i])
            else:
                # print(f'alice is watering i: {i}')
                alice = water(alice, capacityA, plants[i])
                # print(f'alice water left: {alice}')
                # print(f'bob is watering i: {i}')
                bob = water(bob, capacityB, plants[N - i - 1])
                # print(f'bob water left: {bob}')

        return refills


sol = Solution()
print(sol.minimumRefill(plants=[2, 2, 3, 3], capacityA=5, capacityB=5) == 1)
print(sol.minimumRefill(plants=[2, 2, 3, 3], capacityA=3, capacityB=4) == 2)
print(sol.minimumRefill(plants=[5], capacityA=10, capacityB=8) == 0)
print(sol.minimumRefill(plants=[1, 2, 4, 4, 5], capacityA=6, capacityB=5) == 2)
print(sol.minimumRefill(plants=[2, 2, 5, 2, 2], capacityA=5, capacityB=5) == 1)
