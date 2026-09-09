class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        if len(s)!=len(t):
            return False
        for letter in s:
            seen[letter]=seen.get(letter,0)+1
        for letter in t:
            if letter not in seen:
                return False
            elif seen[letter]==0:
                return False
            seen[letter]-=1
        return True

        