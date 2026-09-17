# OPTIMAL
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set(nums)
        longest=0

        for number in nums:
            if number-1 not in seen:
                length=0
                while(number+length) in seen:
                    length+=1
                longest = max(length,longest)
        return longest

