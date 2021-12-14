from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        intermediate, total_gas = 0, 0
        should_start = 0
        for i in range(len(gas)):
            at_i = gas[i] - cost[i]
            intermediate += at_i

            if intermediate < 0:
                total_gas += intermediate
                intermediate = 0
                should_start = i + 1

        total_gas += intermediate

        return should_start % len(gas) if total_gas >= 0 else -1


sol = Solution()
print(sol.canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))
print(sol.canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]))
print(sol.canCompleteCircuit(gas=[3, 1, 1], cost=[1, 2, 2]))
