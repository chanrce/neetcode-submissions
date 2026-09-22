class Solution:
    def findMin(self, nums: List[int]) -> int:
        #assume first number is the min
        res = nums[0]
        l, r = 0, len(nums) - 1
        
        # checks if current part of array is sorted.
        # if the l is less than right, then the whole section is normally sorted
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            # gets middle index
            m = (l + r) // 2
            res = min(res, nums[m])
            # checks if left half is sorted
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        return res