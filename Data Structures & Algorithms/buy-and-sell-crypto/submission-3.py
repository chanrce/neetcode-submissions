class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l is buy, r is sell. r = 1 bc after buy
        l = 0
        r = 1
        maxP = 0
        #while r is in array
        while r < len(prices):
            #print("BEFORE | buy:", prices[l], "sell:", prices[r], "maxP:", maxP)
            if prices[r]>prices[l]:
                maxP=max(maxP, prices[r]-prices[l])
            else:
                # if sell is less than buy, buy cheaper
                # update buy with cheaper price
                l=r
                #print("l was updated")
            #print("AFTER  | buy:", prices[l], "sell:", prices[r], "maxP:", maxP)
            #print("------")
            r=r+1
        return maxP



