from typing import List
from collections import defaultdict, deque


class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.indices = defaultdict(list)
        for i, e in enumerate(arr):
            self.indices[e].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        indices = deque(self.indices.get(value, []))
        if not indices:
            return 0

        while indices and left > indices[0]:
            indices.popleft()
        while indices and right < indices[-1]:
            indices.pop()

        return len(indices)



# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
