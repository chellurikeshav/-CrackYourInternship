class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_val = 0
        n = len(prices)
        
        buy, sell = 0,1
        
        while sell < n:
            if prices[buy]<prices[sell]:
                max_val = max(max_val,prices[sell]-prices[buy])
            else:
                buy = sell
            
            sell+=1
        return max_val
        