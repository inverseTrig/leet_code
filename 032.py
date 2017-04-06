# Longest Valid Parentheses

class Solution(object):
    def longestValidParentheses(self, s)
        n = len(s)
	longest = 0
	temp = []
	
	for i in xrange(n):
	    if s[i] == "(":
		temp.append(i)
	    else:
		if temp != []:
		    if s[temp[-1]] == "(":
			del temp[-1]
		    else:
			temp.append(i)
		else:
		    temp.append(i)
	
	if temp == []:
	    longest = n
	else:
	    a, b = n, 0
	    while temp != []:
		b = temp[-1]
		del temp[-1]
		longest = max(longest, a - b - 1)
		a = b
	    longest = max(longest, a)
	
	return longest
