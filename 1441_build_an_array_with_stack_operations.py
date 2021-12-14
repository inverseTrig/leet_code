from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        idx = 0
        for i in range(1, n + 1):
            # print(f'i: {i}, idx: {idx}')
            if idx >= len(target):
                break

            if target[idx] == i:
                result.append("Push")
                idx += 1

            else:
                result.append("Push")
                result.append("Pop")

        return result


sol = Solution()
print(sol.buildArray(target=[1, 3], n=3))
print(sol.buildArray(target=[1, 2, 3], n=3))
print(sol.buildArray(target=[1, 2], n=4))
print(sol.buildArray(target=[2, 3, 4], n=4))
