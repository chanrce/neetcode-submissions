class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        copy = nums1[:m]
        copy.extend(nums2[:n])
        copy.sort()

        nums1[:] = copy