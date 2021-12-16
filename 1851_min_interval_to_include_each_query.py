import heapq

from typing import List


class Solution:
    def minInterval(self,
                    intervals: List[List[int]],
                    queries: List[int],
                    ) -> List[int]:
        # Sort intervals in decreasing order of left end
        intervals.sort(reverse=True)

        # Sort queries and track their original index
        sorted_queries = sorted(enumerate(queries), key=lambda y: y[1])
        ans = [-1] * len(queries)

        # Heap of (size, right_end) pairs
        active_intervals = []

        for orig_index, point in sorted_queries:

            # Clear all "expired" intervals [start, end] with end < point
            while active_intervals and active_intervals[0][1] < point:
                heapq.heappop(active_intervals)

            # Process new intervals in order of start;
            # add (size, end) of interval to heap
            while intervals and intervals[-1][0] <= point:
                x, y = intervals.pop()
                # If interval is not expired
                if y >= point:
                    heapq.heappush(active_intervals, (y - x + 1, y))

            if active_intervals:
                ans[orig_index] = active_intervals[0][0]

        return ans


sol = Solution()
print(sol.minInterval(intervals=[[1, 4], [2, 4], [
      3, 6], [4, 4]], queries=[2, 3, 4, 5]))
