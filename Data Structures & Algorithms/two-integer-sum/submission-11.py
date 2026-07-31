class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       seen = {}
       for i,v in enumerate(nums):
            ans=target-nums[i]
            # check dict membership
            if ans in seen:
                return [seen[ans], i]

            # otherwise, add to the dict
            seen[v]=i