# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        post = None
        while slow:
            tmp = slow.next
            slow.next = post
            post, slow = slow, tmp

        while post and head:
            if post.val != head.val:
                return False
            post, head = post.next, head.next
        return True
