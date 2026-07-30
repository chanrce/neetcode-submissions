class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # loop thru s and add all chars in s to a dict
        seen = {}

        if len(s)!=len(t):
            return False

        for char in s:
            if char not in seen:
                seen[char]=0
            seen[char]+=1
        # loop thru t and check if those match dictionary vals or not
            # decrement from dict count each time it is seen
        for char in t:
            if char not in seen:
                return False
            if seen[char]==0:
                return False
            if char in seen:
                seen[char]-=1
        return True

