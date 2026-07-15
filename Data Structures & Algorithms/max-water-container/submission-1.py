class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # stores max area found
        res=0
        # left starts at first index, right at last index of array
        # starting at far end maximizes one contraint: the width
        l,r=0, len(heights)-1
        
        #r-l is the width of the container
        # height is limited by shorter of the two lines, hence min heigths
        while l<r:
            # need the min of the heights since this limits the container height
            area = (r-l) * min(heights[l], heights[r])
            res = max(res,area)
            # keep the height of the taller line
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return res
