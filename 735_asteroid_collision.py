from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            # print(f'working on ast {ast}')
            # print(f'stack is {stack}')
            while stack and stack[-1] > 0 and ast < 0:
                # Previous going right, current going left, collision
                prev = stack.pop()
                # print(f'found collision, popped {prev}')
                if prev + ast > 0:
                    ast = prev
                elif prev + ast == 0:
                    ast = 0

            if ast:
                stack.append(ast)

        return stack


sol = Solution()
print(sol.asteroidCollision(asteroids=[5, 10, -5]))
print(sol.asteroidCollision(asteroids=[8, -8]))
print(sol.asteroidCollision(asteroids=[10, 2, -5]))
print(sol.asteroidCollision(asteroids=[-2, -1, 1, 2]))
print(sol.asteroidCollision(asteroids=[-2, 1, 1, -1]))
