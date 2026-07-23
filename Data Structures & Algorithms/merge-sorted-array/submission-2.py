class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        copy=nums1[0:m]
        copy.extend(nums2[0:n])
        copy.sort()
        nums1[:]=copy
