from typing import List
import heapq


class Solution:
    def maxAverageRatio(self,
                        classes: List[List[int]],
                        extraStudents: int,
                        ) -> float:
        def possible_profit(a, b):
            return (a + 1) / (b + 1) - (a / b)

        heap = []
        for numer, denom in classes:
            heap.append((-possible_profit(numer, denom),
                         numer,
                         denom,
                         ))
        heapq.heapify(heap)

        for _ in range(extraStudents):
            _, numer, denom = heapq.heappop(heap)
            heapq.heappush(heap,
                           (-possible_profit(numer + 1, denom + 1),
                            numer + 1,
                            denom + 1,
                            ))

        return sum(numer / denom for _, numer, denom in heap) / len(heap)


sol = Solution()
print(sol.maxAverageRatio(classes=[[1, 2], [3, 5], [2, 2]], extraStudents=2))
