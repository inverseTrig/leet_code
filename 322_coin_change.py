from typing import List
from heapq import heapify, heappop


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        heap = [-coin for coin in coins]
        heapify(heap)

        change_count = 0
        while heap and amount > 0:
            change = -heappop(heap)
            print(f"-----------change: {change}")
            if amount >= change:
                print(f"amount before: {amount}")
                change_count += amount // change
                print(f"change_count: {change_count}")
                amount %= change
                print(f"amount after: {amount}")

        return change_count if amount == 0 else -1


sol = Solution()
print(sol.coinChange(coins=[186, 419, 83, 408], amount=6249))
