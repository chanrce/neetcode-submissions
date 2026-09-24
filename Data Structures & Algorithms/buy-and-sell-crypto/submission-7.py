class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #left=buy, right = sell
        l,r=0,1
        maxP=0

        while r<len(prices):
            #profitable?
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                maxP=max(maxP,profit)
            #replace the buy day with cheaper price
            else:
                l=r
            r+=1
        return maxP