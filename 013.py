# Roman to Integer

class Solution(object):
    def romanToInt(self, s):
	total = 0
	if "IV" in s:
	    total -= 2
	if "IX" in s:
	    total -= 2
	if "XL" in s:
	    total -= 20
	if "XC" in s:
	    total -= 20
	if "CD" in s:
	    total -= 200
	if "CM" in s:
	    total -= 200
	
	for i in range(0, len(s)):
	    if s[i] == "M":
		total += 1000
	    elif s[i] == "D":
		total += 500
	    elif s[i] == "C":
		total += 100
	    elif s[i] == "L":
		total += 50
	    elif s[i] == "X":
		total += 10
	    elif s[i] == "V":
		total += 5
	    elif s[i] == "I":
		total += 1
	
	return total
