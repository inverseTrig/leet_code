# Multiply Strings

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
	z = []
        if num1 == "" or num2 == "":
	    return "0"
	else:
	    for x in range(len(num1), 0, -1):
		for y in range(len(num2), 0, -1):
		    exx = int(num1[x-1])
		    wyy = int(num2[y-1])
		    
		    print(exx, wyy)
		    z.append(int(num1[x-1]) * int(num2[y-1]))
	    return z

print(Solution().multiply("21", "12"))
