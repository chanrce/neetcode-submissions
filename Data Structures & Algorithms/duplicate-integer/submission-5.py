class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        stored = set()
        for i in nums:
            if i not in stored:
                stored.add(i)
            else:
                return True
        return False

