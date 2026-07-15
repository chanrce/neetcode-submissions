class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=[]

        for i in nums:
            print (i)
            print("current lisr", seen)
            if i in seen:
                return True
            if i not in seen:
                seen.append(i)
        return False