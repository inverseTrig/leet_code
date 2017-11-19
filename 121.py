# Best Time to Buy and Sell Stock

class Solution(object):
	def maxProfit(self, prices):
		if prices is None or prices == []:
			return 0
			
		sell = buy = prices[-1]
		profit = 0
		for i in range(len(prices)-1, -1, -1):
			if sell < prices[i]:
				sell = buy = prices[i]
			buy = prices[i]
			if sell - buy > profit:
				profit = sell - buy
		return profit
