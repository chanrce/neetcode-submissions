class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create set
        seen = set()
        # go through nums
        for number in nums:
            # if in set, contains duplicate so return true
            if number in seen:
                return True
            # save each in set
            seen.add(number)
            #else, return false
        return False