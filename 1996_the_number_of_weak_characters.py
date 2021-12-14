class Solution:
    def numberOfWeakCharacters(self, properties) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))

        current_max = 0
        count = 0

        for _, defense in properties:
            if defense < current_max:
                count += 1
            else:
                current_max = defense

        return count
