# Teemo Attacking

class Solution(object):
	def findPoisonedDuration(self, timeSeries, duration):
		if timeSeries == [] or duration == 0:
			return 0
		
		attacked = timeSeries[0]
		poisonedUntil = attacked + duration - 1
		counter = duration
		
		for i in range(1, len(timeSeries)):
			if timeSeries[i] <= poisonedUntil:
				counter += timeSeries[i] - attacked
				attacked = timeSeries[i]
				poisonedUntil = attacked + duration - 1
				
			else:
				attacked = timeSeries[i]
				poisonedUntil = attacked + duration - 1
				counter += duration
		return counter
