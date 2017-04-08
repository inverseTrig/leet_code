# Swap Nodes in Pairs

class ListNode(object):
    def __init__(self, x):
	self.val = x
	self.next = None
	
	
class Solution(object):
    def swapPairs(self, head):
        if head is None or head.next is None:
	    return head
	else:
	    n = head.next
	    head.next = Solution().swapPairs(head.next.next)
	    n.next = head
	    return n
