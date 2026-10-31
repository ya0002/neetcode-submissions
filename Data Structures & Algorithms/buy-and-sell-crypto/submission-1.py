class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp,profit = prices[0],0
        for i in prices[1:]:
            if i<minp:
                minp = i
            else:
                profit = max(profit,i-minp)
        return profit