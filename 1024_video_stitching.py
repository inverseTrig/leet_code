from typing import List
import heapq


class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        heapq.heapify(clips)

        left, right = 0, 0
        clippings = 0

        while clips:
            new_left, new_right = heapq.heappop(clips)
            print(f'new_left, new_right: {new_left}, {new_right}')

            while clips and left <= new_left <= right:
                new_left, new_right = heapq.heappop(clips)
                print(f'new_left, new_right: {new_left}, {new_right}')
                right = max(right, new_right)
                print(f'right: {right}')
                if right >= time:
                    return clippings

            left = new_left
            clippings += 1

            # if left == new_left and new_right > right:
            #     right = new_right
            # if left < new_left < right and right < new_right:
            #     clippings += 1
            #     left = new_left
            #     right = max(new_right, right)

        return clippings if right >= time else -1


sol = Solution()
# print(sol.videoStitching(clips=[[0, 2], [4, 6], [
#       8, 10], [1, 9], [1, 5], [5, 9]], time=10))
# print(sol.videoStitching(clips=[[0, 4], [2, 8]], time=5))
# print(sol.videoStitching(clips=[[0, 1], [1, 2]], time=5))

c = [[0, 1], [6, 8], [0, 2], [5, 6], [0, 4], [0, 3], [6, 7], [1, 3],
     [4, 7], [1, 4], [2, 5], [2, 6], [3, 4], [4, 5], [5, 7], [6, 9]]
t = 9
print(sol.videoStitching(clips=c, time=t))
