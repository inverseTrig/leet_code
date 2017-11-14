# Plus One

class Solution(object):
	def plusOne(self, digits):
		# Reverse the digits as it would be easier to extend the array if needed later on
		digits = list(reversed(digits))
		
		# Add one!
		digits[0] += 1
		
		# But now check if any of the numbers changed to more than 1 digit, and if so, move it to the next
		for i in range(0, len(digits)):
			if digits[i] > 9:
				digits[i] %= 10
				if i != len(digits)-1:
					digits[i+1] += 1
				else:
					digits.append(1)
					
		# Reverse it back!
		digits = list(reversed(digits))
		
		return digits
