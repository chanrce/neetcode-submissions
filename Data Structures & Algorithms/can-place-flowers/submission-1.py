class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # new array with 0s at ends
        array=[0]+flowerbed+[0]
        print(array)
        
        # iterate through the array from original list indices
        for index in range(1,len(array)-1):
            if array[index]==0 and array[index-1]==0 and array[index+1]==0:
                # update that value to 1
                array[index]=1
                # update count
                n-=1
        return n<=0
