from typing import List
from functools import lru_cache


class Solution:
    def smallestSufficientTeam(self,
                               req_skills: List[str],
                               people: List[List[str]],
                               ) -> List[int]:
        skill_mask = {skill: 2 ** i for i, skill in enumerate(req_skills)}

        def get_mask(skillset: List[str]):
            val = 0
            for skill in skillset:
                val += skill_mask.get(skill, 0)
            return val

        req = 2 ** (len(req_skills)) - 1
        people_mask = [get_mask(p) for p in people]

        @lru_cache(None)
        def fn(i, current):
            if current == 0:
                return []

            if i == len(people_mask):
                return [0] * 99

            if not (current & people_mask[i]):
                return fn(i + 1, current)

            return min(fn(i + 1, current),
                       [i] + fn(i + 1, current & ~people_mask[i]),
                       key=len,
                       )

        return fn(0, req)


sol = Solution()
print(sol.smallestSufficientTeam(req_skills=["java", "nodejs", "reactjs"], people=[["java"], ["nodejs"], ["nodejs", "reactjs"]]))  # noqa
print(sol.smallestSufficientTeam(req_skills=["algorithms", "math", "java", "reactjs", "csharp", "aws"], people=[["algorithms", "math", "java"], ["algorithms", "math", "reactjs"], ["java", "csharp", "aws"], ["reactjs", "csharp"], ["csharp", "math"], ["aws", "java"]]))  # noqa
