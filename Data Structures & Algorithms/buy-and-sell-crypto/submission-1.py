class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp=101
        profit=0
        for i in range((len(prices))):
            minp=min(minp,prices[i])
            profit=max(profit,prices[i]-minp)
        return profit
        