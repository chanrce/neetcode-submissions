class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # set for seen
        seen=set()
        for val in nums:
            if val in seen:
                return True
            else:
                seen.add(val)
                #print(seen)
        return False