#OPTIMAL
# nums = [4, 5, 6, 7, 0, 1, 2]
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # track best min so far
        res=nums[0]
        l,r=0,len(nums)-1
        # while search area exists:
        while l<=r:
            #if already sorted
            if nums[l]<nums[r]:
                #check leftmost number:
                res=min(res,nums[l])
                break
            # calculate midpoint
            m=(l+r)//2
            #save nums[m] in case it's the min, since a new search range won't include it
            res = min(res, nums[m])
            #if sorted correctly
            if nums[l]<=nums[m]:
                l=m+1
            else:
                r=m-1
        return res
                
                

