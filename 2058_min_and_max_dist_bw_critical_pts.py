from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self,
                                   head: Optional[ListNode],
                                   ) -> List[int]:
        if not head:
            return [-1, -1]
        pass

        one = two = None
        thr = head

        idx = 0
        crtcl_pts = []

        while thr.next:
            one, two, thr = two, thr, thr.next
            if one and two and thr:
                if one.val < two.val > thr.val \
                        or one.val > two.val < thr.val:
                    crtcl_pts.append(idx)
            idx += 1

        if len(crtcl_pts) < 2:
            return [-1, -1]

        sml, lrg = float('inf'), crtcl_pts[-1] - crtcl_pts[0]
        for i in range(1, len(crtcl_pts)):
            sml = min(crtcl_pts[i] - crtcl_pts[i - 1], sml)

        return [sml, lrg]
