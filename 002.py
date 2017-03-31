
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        if l1 == None:
	    return l2
	if l2 == None:
	    return l1
	
	pointer = l1
	carryOver = (l1.val + l2.val) // 10
	l1.val = (l1.val + l2.val) % 10
	
	while l1.next != None and l2.next != None:
	    carryOver += l1.next.val
	    carryOver += l2.next.val
	    
	    l1.next.val = carryOver % 10
	    carryOver = carryOver // 10
	    
	    l1 = l1.next;
	    l2 = l2.next;
	    
	if l1.next == None:
	    l1.next = l2.next
	    
	while l1.next != None:
	    carryOver+= l1.next.val
	    l1.next.val = carryOver % 10
	    carryOver = carryOver // 10
	    l1 = l1.next
	
	if carryOver > 0:
	    l1.next = ListNode(carryOver)
	    
	return pointer
