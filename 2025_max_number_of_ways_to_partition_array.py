from itertools import accumulate
from typing import List
from collections import Counter


class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        print(f'Nums: {nums}')
        prefix_sums = list(accumulate(nums))
        total_sum = prefix_sums[-1]
        best = 0
        if total_sum % 2 == 0:
            best = prefix_sums[:-1].count(total_sum // 2)  # If no change

        print(f'Prefix Sums: {prefix_sums}')
        print(f'Total Sum: {total_sum}')

        print(f'Best: {best}')

        after_counts = Counter(total_sum - 2 * prefix_sum
                               for prefix_sum in prefix_sums[:-1])
        before_counts = Counter()

        print(f'After Counts: {after_counts}')
        print(f'Before Counts: {before_counts}')

        best = max(best, after_counts[k - nums[0]])  # If we change first num

        print(f'best: {best}')

        for prefix, x in zip(prefix_sums, nums[1:]):
            print(f'prefix: {prefix}\tx: {x}')
            gap = total_sum - 2 * prefix
            after_counts[gap] -= 1
            before_counts[gap] += 1

            best = max(best, after_counts[k - x] + before_counts[x - k])
            print(f'best: {best}')

        return best


sol = Solution()
print(sol.waysToPartition(
    nums=[22, 4, -25, -20, -15, 15, -16, 7, 19, -10, 0, -13, -14], k=-33))
