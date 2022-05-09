class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right= 0,1
        profit=0
        
        while right<len(prices):
            curr= prices[right]-prices[left]
            if prices[left]<prices[right]:
                profit= max(profit,curr)
            else:
                left=right
            right+=1
        
        return profit