class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, value in enumerate(nums):
            ans=target-nums[index]
            if ans in seen:
                return[seen[ans],index]

            seen[value]=index
