# Integer to Roman

import string

class Solution(object):
    def intToRoman(self, num):
        while num != 0:
	    
	    romanStr = ""
	    countM, countD, countC, countL, countX, countV, countI = 0, 0, 0, 0, 0, 0, 0
	    
	    if num > 999:
		countM = num / 1000
		num %= 1000
	    
	    if num > 499:
		countD = num / 500
		num %= 500
		
	    if num > 99:
		countC = num / 100
		num %= 100
	    
	    if num > 49:
		countL = num / 50
		num %= 50
	    
	    if num > 9:
		countX = num / 10
		num %= 10
	    
	    if num > 4:
		countV = num / 5
		num %= 5
	    
	    if num > 0:
		countI = num / 1
		num %= 1
	
	for i in range(0, countM):
	    romanStr += "M"
	for i in range(0, countD):
	    romanStr += "D"
	for i in range(0, countC):
	    romanStr += "C"
	for i in range(0, countL):
	    romanStr += "L"
	for i in range(0, countX):
	    romanStr += "X"
	for i in range(0, countV):
	    romanStr += "V"
	for i in range(0, countI):
	    romanStr += "I"
	
	if "DCCCC" in romanStr:
	    romanStr = string.replace(romanStr, 'DCCCC', 'CM')
	if "CCCC" in romanStr:
	    romanStr = string.replace(romanStr, 'CCCC', 'CD')
	if "LXXXX" in romanStr:
	    romanStr = string.replace(romanStr, 'LXXXX', 'XC')
	if "XXXX" in romanStr:
	    romanStr = string.replace(romanStr, 'XXXX', 'XL')
	if "VIIII" in romanStr:
	    romanStr = string.replace(romanStr, 'VIIII', 'IX')
	if "IIII" in romanStr:
	    romanStr = string.replace(romanStr, 'IIII', 'IV')
	    
	return romanStr
    
	
print(Solution().intToRoman(999))
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
