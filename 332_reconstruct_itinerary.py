from typing import List
from collections import defaultdict
from sortedcontainers import SortedList


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        paths = defaultdict(SortedList)

        for origin, destination in tickets:
            paths[origin].add(destination)

        trip = ["JFK"]
        ending = []
        while len(trip) < len(tickets) + 1:
            while trip and not paths[trip[-1]]:
                ending.append(trip.pop())

            if not trip:
                break

            _destination = paths[trip[-1]].pop(0)
            if _destination in paths:
                trip.append(_destination)
            else:
                ending.append(_destination)

        return trip + list(reversed(ending))


sol = Solution()
print(sol.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))  # noqa
print(sol.findItinerary([["EZE", "TIA"], ["EZE", "HBA"], ["AXA", "TIA"], ["JFK", "AXA"], ["ANU", "JFK"], ["ADL", "ANU"], ["TIA", "AUA"], ["ANU", "AUA"], ["ADL", "EZE"], ["ADL", "EZE"], ["EZE", "ADL"], ["AXA", "EZE"], ["AUA", "AXA"], ["JFK", "AXA"], ["AXA", "AUA"], ["AUA", "ADL"], ["ANU", "EZE"], ["TIA", "ADL"], ["EZE", "ANU"], ["AUA", "ANU"]]))  # noqa


# import collections


# class Solution(object):
#     def findItinerary(self, tickets):
#         targets = collections.defaultdict(list)
#         for a, b in sorted(tickets)[::-1]:
#             targets[a].append(b)

#         route, stack = [], ['JFK']
#         while stack:
#             print('start of while stack')
#             while targets[stack[-1]]:
#                 stack.append(targets[stack[-1]].pop())
#                 print(f'stack: {stack}')
#             route.append(stack.pop())
#             print(f'route: {route}\n')
#         return route[::-1]


# sol = Solution()
# print(sol.findItinerary([["EZE", "TIA"], ["EZE", "HBA"], ["AXA", "TIA"], ["JFK", "AXA"], ["ANU", "JFK"], ["ADL", "ANU"], ["TIA", "AUA"], ["ANU", "AUA"], ["ADL", "EZE"], ["ADL", "EZE"], ["EZE", "ADL"], ["AXA", "EZE"], ["AUA", "AXA"], ["JFK", "AXA"], ["AXA", "AUA"], ["AUA", "ADL"], ["ANU", "EZE"], ["TIA", "ADL"], ["EZE", "ANU"], ["AUA", "ANU"]]))  # noqa
