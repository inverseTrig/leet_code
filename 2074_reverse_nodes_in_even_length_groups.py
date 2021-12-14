from typinng import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) \
            -> Optional[ListNode]:
        while head:
            counter = 1
            if counter % 2 == 0:
                for i in range(counter):
                    # TODO: FLIP
                    pass

