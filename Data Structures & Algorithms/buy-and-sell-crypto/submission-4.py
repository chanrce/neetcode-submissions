
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)): 
                profit=prices[j]-prices[i]
                if profit<0:
                    maxi=max(0,maxi)
                else:
                    maxi=max(maxi,profit)
                print(f"indices{i},{j},values{prices[i]},{prices[j]},profit,{profit}")
        return maxi

        