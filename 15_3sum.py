from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()

        negatives, positives, zeroes = [], [], []
        for num in nums:
            if num < 0: negatives.append(num)
            elif num > 0: positives.append(num)
            else: zeroes.append(num)

        print(positives)
        print(negatives)
        print(zeroes)

        if len(zeroes) >= 3:
            result.add(tuple([0, 0, 0]))

        N, P = set(negatives), set(positives)

        if zeroes:
            for n in negatives:
                if -n in positives: result.add(tuple(sorted([n, -n, 0])))

        for i in range(len(negatives)):
            for j in range(i + 1, len(negatives)):
                target = negatives[i] + negatives[j]
                if -target in P:
                    result.add(tuple(sorted([negatives[i], negatives[j], -target])))

        for i in range(len(positives)):
            for j in range(i + 1, len(positives)):
                target = positives[i] + positives[j]
                if -target in N:
                    result.add(tuple(sorted([positives[i], positives[j], -target])))


        return result

sol = Solution()
print(sol.threeSum(nums = [-1,0,1,2,-1,-4]))