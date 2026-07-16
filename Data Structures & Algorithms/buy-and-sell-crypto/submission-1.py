class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for buy in range(len(prices)):
            #print("buy inx: ", buy, "price: ",prices[buy])
            for sell in range(buy+1,len(prices)):
                #print("sell inx: ", sell, "price: ",prices[sell])
                if prices[sell]-prices[buy]>profit:
                    #print("PROFIT UPDATE")
                    profit=prices[sell]-prices[buy]
                    #print(profit)
        return profit
                
        


        