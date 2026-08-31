class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # make result array
        res=[]
        # running prod of everything to the left
        prefix=1
        # loop left to right
        for i in range(len(nums)):
            res.append(prefix)
            prefix*=nums[i]


        # running prod of everything to the right
        postfix = 1
        # loop right to left
        # start at 3, stop before -1, go down -1 each
        for i in range(len(nums)-1, -1,-1):
            res[i]=postfix*res[i]
            postfix*=nums[i]
        return res