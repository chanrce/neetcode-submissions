class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # splice for n (nums1 must stay the original list)
        nums2 = nums2[:n]

        # copy
        copy = []

        # two pointers
        # p1 for nums1
        p1 = 0
        # p2 for nums2
        p2 = 0

        while p1 < m and p2 < n:
            if nums1[p1] == nums2[p2]:
                copy.append(nums1[p1])
                copy.append(nums2[p2])
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                copy.append(nums1[p1])
                p1 += 1
            else:
                copy.append(nums2[p2])
                p2 += 1

        # remaining nums1 or nums2 just add to end of copy
        if p1 < m:
            copy.extend(nums1[p1:m])
        else:
            copy.extend(nums2[p2:n])

        # replace the contents of the original nums1
        nums1[:] = copy