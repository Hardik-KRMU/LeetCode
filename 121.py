class Solution:
    def maxProfit(self, prices):
        max_profit = 0
        curr = 0
        
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            curr = max(0, curr + diff)
            max_profit = max(max_profit, curr)
        
        return max_profit