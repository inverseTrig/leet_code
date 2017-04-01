# ZigZag Conversion

class Solution(object):
    def convert(self, s, numRows):
	if len(s) == 1 or numRows == 1:
	    return s
	    
	combined = [""] * numRows
	n = numRows - 1
	returnString = ""
	
        for i in range(0,len(s)):
	    
	    if i % (2 * n) < numRows:
		combined[i % (2 * n)] += s[i]
	    else:
		combined[abs( (i % n) - n )] += s[i]
	    
	for j in range(0, len(combined)):
	    returnString += combined[j]
	
	return returnString
	
print(Solution().convert("PAYPALISHIRING", 3))
