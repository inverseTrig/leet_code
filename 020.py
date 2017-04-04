# Valid Parentheses

class Solution(object):
    def isValid(self, s):
	stack = [""]
	
	if len(s) % 2 != 0:
	    return False
	
        for i in xrange(len(s)):
	    
	    if s[i] == "[":
		stack.append("]")
	    elif s[i] == "(":
		stack.append(")")
	    elif s[i] == "{":
		stack.append("}")
	    else:
		pass
	    if s[i] == "]":
		if stack[-1] == "]":
		    del stack[-1]
		else:
		    return False
	    elif s[i] == ")":
		if stack[-1] == ")":
		    del stack[-1]
		else:
		    return False
	    elif s[i] == "}":
		if stack[-1] == "}":
		    del stack[-1]
		else:
		    return False
	    else:
		pass
		
	if stack == [""]:
	    return True
	return False
