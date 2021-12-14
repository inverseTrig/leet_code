from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self,
                  numCourses: int,
                  prerequisites: List[List[int]],
                  ) -> bool:

        NOT_VISITED = 0
        PROCESSING = -1
        PROCESSED = 1

        course_map = defaultdict(list)
        for course, prereq in prerequisites:
            course_map[prereq].append(course)

        state = [NOT_VISITED] * numCourses

        def take_course(prereq):
            if state[prereq] == PROCESSING:
                return False

            if state[prereq] == PROCESSED:
                return True

            state[prereq] = PROCESSING

            for course in course_map[prereq]:
                if not take_course(course):
                    return False

            state[prereq] = PROCESSED
            return True

        for i in range(numCourses):
            if not take_course(i):
                return False

        return True


sol = Solution()
print(sol.canFinish(numCourses=2, prerequisites=[[1, 0]]))
print(sol.canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]]))
