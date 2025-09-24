# Last updated: 9/24/2025, 12:46:06 AM
'''
Two Pointer solution. 

first create the pointers l r (0,1). Then calculate the profit and keep checking if it is greater than the max_p. (if r > l). Else l = r. 

Then return max_p
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            r += 1
        return max_profit

