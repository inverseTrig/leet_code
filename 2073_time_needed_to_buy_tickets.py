from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        front, back = tickets[:k + 1], tickets[k + 1:]

        time_took = 0
        for n in front:
            time_took += min(n, tickets[k])

        for n in back:
            time_took += min(n, tickets[k] - 1)

        return time_took


sol = Solution()
print(sol.timeRequiredToBuy(tickets=[2, 3, 2], k=2))
