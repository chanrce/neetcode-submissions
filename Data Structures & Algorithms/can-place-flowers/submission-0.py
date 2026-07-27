class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for index,value in enumerate(flowerbed):
            if n==0:
                return True
            elif index==0 and flowerbed[index]==0:
                if len(flowerbed)==1:
                    flowerbed[index]=1
                    n-=1
                elif flowerbed[index+1]==0:
                    flowerbed[index]=1
                    n-=1
            elif index==len(flowerbed)-1 and flowerbed[index]==0:
                if flowerbed[index-1]==0:
                    flowerbed[index]=1
                    n-=1
            elif flowerbed[index]==0:
                if flowerbed[index+1]==0 and flowerbed[index-1]==0:
                    flowerbed[index]=1
                    n-=1
        if n==0:
            return True
        return False
        
        

        