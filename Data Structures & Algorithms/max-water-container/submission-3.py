class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #store max height
        max_height=0
        #left pointer at index 0
        left=0
        #right pointer at last position
        right=len(heights)-1
        #while l<r
        while left<right:
            #calc the area: min height (l,r)*(r-l)
            area=min(heights[left],heights[right])*(right-left)
            #if area>max: update max
            if area>max_height:
                max_height=area
            #if l[height]<r[height]:
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        #return max
        return max_height
            