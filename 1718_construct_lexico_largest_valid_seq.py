from typing import List


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        m = 2 * n - 1
        step, used = [0] * m, [False] * (n + 1)

        def dfs(i):
            print(f'\t--- i is {i}')
            if i == m:
                return all(step)
            if step[i]:
                return dfs(i + 1)
            for x in range(n, 0, -1):
                print(f'\t\t--- x is {x}')
                j = i if x == 1 else i + x
                if not used[x] and j < m and not step[j]:
                    step[i], step[j], used[x] = x, x, True
                    print(f'Step: {step}')
                    print(f'Used: {used}')
                    if dfs(i + 1):
                        return True
                    step[i], step[j], used[x] = 0, 0, False
            return False
        dfs(0)
        return step


sol = Solution()
# print(sol.constructDistancedSequence(n=3))
print(sol.constructDistancedSequence(n=5))
