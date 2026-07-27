class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # new array with 0s at ends
        array=[0]+flowerbed+[0]
        print(array)
        
        # iterate through the array from original list indices
        for index in range(1, len(array)-1):
            print("Start:", index, "n =", n)

            if n == 0:
                print("Returning True")
                return True

            if array[index] == 0 and array[index-1] == 0 and array[index+1] == 0:
                print("Planting!")
                array[index] = 1
                n -= 1
            if n==0:
                return True
        return False