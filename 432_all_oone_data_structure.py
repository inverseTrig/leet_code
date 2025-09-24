from collections import Counter

class AllOne:

    def __init__(self):
        self.counter = Counter()
        self.max = None
        self.min = None

    def inc(self, key: str) -> None:
        self.counter[key] += 1
        self.max = None
        self.min = None

    def dec(self, key: str) -> None:
        if self.counter[key] == 1:
            del self.counter[key]
        else:
            self.counter[key] -= 1
        self.max = None
        self.min = None

    def getMaxKey(self) -> str:
        if self.max:
            return self.max
        max_key_pair = self.counter.most_common(1)
        if not max_key_pair:
            return ""

        maximum = max_key_pair[0][0]
        self.max = maximum
        return maximum

    def getMinKey(self) -> str:
        if self.min:
            return self.min
        most_common = self.counter.most_common()
        if not most_common:
            return ""

        minimum = most_common[-1][0]
        self.min = minimum
        return minimum



# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
