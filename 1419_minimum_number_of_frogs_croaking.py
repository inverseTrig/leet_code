class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        mask = {'c': 1, 'r': 2, 'o': 4, 'a': 8, 'k': 16}
        states, max_len = [], 0
        for char in croakOfFrogs:
            # print(f'at char {char}')
            prereq = mask[char] - 1
            if prereq:
                if prereq not in states:
                    return -1
                states.remove(prereq)
            _new = prereq | mask[char]
            if _new != 31:
                states.append(_new)
            # print(states)
            max_len = max(max_len, len(states))
        return max_len if not states else -1


sol = Solution()
print(sol.minNumberOfFrogs(croakOfFrogs="croakcroak"))
print(sol.minNumberOfFrogs(croakOfFrogs="crcoakroak"))
print(sol.minNumberOfFrogs(croakOfFrogs="croakcrook"))
print(sol.minNumberOfFrogs(croakOfFrogs="croakcroa"))
