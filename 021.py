# Merge Two Sorted Lists

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
	
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
	    return l2
	if l2 is None:
	    return l1
	
	if l1.val < l2.val:
	    l1.next = mergeTwoLists(l1.next, l2)
	    return l1
	else:
	    l2.next = mergeTwoLists(l2.next, l1)
	    return l2
	
