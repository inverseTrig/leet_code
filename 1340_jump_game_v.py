from typing import List


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        dp = [1] * len(arr)
        modified = [[val, i] for i, val in enumerate(arr)]
        modified.sort()
        print(modified)
        for val, i in modified:
            for di in [-1, 1]:
                for j in range(i + di, i + d * di + di, di):
                    print(f'-- j: {j}')
                    if not (0 <= j < len(arr) and arr[i] < arr[j]):
                        break
                    dp[i] = max(dp[i], dp[j] + 1)
                    print(f'dp: {dp}')
        return max(dp)


sol = Solution()
print(sol.maxJumps(arr=[6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12], d=2))
print(sol.maxJumps(arr=[3, 3, 3, 3, 3], d=3))
print(sol.maxJumps(arr=[7, 6, 5, 4, 3, 2, 1], d=1))
print(sol.maxJumps(arr=[7, 1, 7, 1, 7, 1], d=2))
print(sol.maxJumps(arr=[66], d=1))
