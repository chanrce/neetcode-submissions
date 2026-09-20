class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # store the maximum area found so far
        max_area = 0

        # start left pointer at index 0
        left = 0

        # start right pointer at the last position
        # starting at opposite ends gives us the biggest possible width first
        right = len(heights) - 1

        # keep checking containers until the two pointers meet
        while left < right:

            # area = height * width
            # the shorter wall determines the container's height,
            # because water would spill over the shorter side
            # width is the distance between the two pointers
            area = min(heights[left], heights[right]) * (right - left)

            # if this area is bigger than our current max, update max
            if area > max_area:
                max_area = area

            # width will only get smaller as we move inward,
            # so we need a chance to find a taller wall to get a bigger area

            # move the pointer at the shorter wall
            # because the shorter wall is currently limiting the height
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        # return the largest area we found
        return max_area