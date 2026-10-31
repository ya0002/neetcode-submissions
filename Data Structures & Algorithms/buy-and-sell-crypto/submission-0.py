class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp,profit = prices[0],0
        for i in prices[1:]:
            minp = min(minp,i)
            profit = max(profit,i-minp)
        return profit