class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        max_profit=0
        for i in range(n):
            for j in range(i+1,n):
                profit=prices[j]-prices[i]
                max_profit=max(max_profit,profit)
        return max_profit
        
prices = [7,6,4,3,1]
s=Solution()
print(s.maxProfit(prices))
 