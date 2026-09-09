class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):

            # skip duplicate values for a
            if i > 0 and a == nums[i - 1]:
                continue

            # start pointers on both ends of everything after a
            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = a + nums[l] + nums[r]

                # sum too big -> need a smaller number
                if threeSum > 0:
                    r -= 1

                # sum too small -> need a bigger number
                elif threeSum < 0:
                    l += 1

                # found a triplet
                else:
                    res.append([a, nums[l], nums[r]])

                    # move left so we can search for another triplet
                    l += 1

                    # skip duplicate left values
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res