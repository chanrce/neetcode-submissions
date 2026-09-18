class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set(nums)
        longest=0

        for number in nums:
            if number-1 not in seen:
                curr=0
                while number+curr in seen:
                    curr+=1
                longest = max(curr,longest)
        return longest
                