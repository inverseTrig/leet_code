from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        if not head.next:
            return head

        index = ListNode(next=head)
        node = index.next
        prev = index

        while node and node.next:
            if node.val == node.next.val:
                node = self.findNextNonDuplicate(node, node.val)
                prev.next = node
            else:
                prev, node = node, node.next
        return index.next


    def findNextNonDuplicate(self, node: ListNode, val: int) -> ListNode:
        while node and node.val == val:
            node = node.next
        return node


sol = Solution()
print(sol.deleteDuplicates(head = [1,2,3,3,4,4,5]))