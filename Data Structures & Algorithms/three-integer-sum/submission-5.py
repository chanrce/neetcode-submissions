class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # result array
        res = []
        #sort array
        nums.sort()
        # go through nums
        for i, value in enumerate(nums):
            # if second in array and not same as prev, skip bc duplicate
            if i>0 and value==nums[i-1]:
                continue
            #pointers on opp ends not including a
            left = i+1
            right = len(nums)-1
            #while l<r
            while left<right:
                #calc threesum
                threeSum = value+nums[left]+nums[right]
                #if equals zero append result
                if threeSum==0:
                    res.append([value,nums[left],nums[right]])
                    #move left pointer
                    left += 1
                    #handle duplicates -- dont get what this is and why we need it
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                #else sum is too big, decrease right and vice versa
                elif threeSum>0:
                    right-=1
                else:
                    left+=1
        return res

            