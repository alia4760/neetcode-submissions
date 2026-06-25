class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minimum = prices[0] 
        for i in range(len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            else:
                diff = prices[i] - minimum
                if diff > profit:
                    profit = diff
        return profit
                    

            
            
        