# Divide Two Integers

class Solution(object):
    def divide(self, dividend, divisor):
        if divisor == 0 or dividend == 0:
	    return 0
	
	count = 0
	neg = 0
	
	if divisor < 0:
	    divisor = abs(divisor)
	    neg += 1
	    
	if dividend < 0:
	    dividend = abs(dividend)
	    neg += 1
	    
	
	while dividend >= divisor:
	    div = divisor
	    i = 1
	    
	    while dividend >= div:
		dividend -= div
		count += i
		i <<= 1
		div <<= 1
	    
	
	if neg == 1:
	    count = -count
	    
	return min(max(-2147483648, count), 2147483647)
