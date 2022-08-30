from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        last = len(prices) -1
        for i in range(last, 0, -1):
            for j in range(i-1, -1, -1):
                p = prices[i] - prices[j]
                if p > profit:
                    profit = p
        return profit            
        
        
result = Solution().maxProfit([7,6,4,3,1])     
print(result)