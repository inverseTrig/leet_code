from collections import deque


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        dq = deque([i for i in range(1, n + 1)])
        turn = 1
        while len(dq) > 1:
            popped = dq.popleft()
            if not turn % k == 0:
                dq.append(popped)
            turn += 1

        return dq.pop()


sol = Solution()
print(sol.findTheWinner(n=5, k=2))
