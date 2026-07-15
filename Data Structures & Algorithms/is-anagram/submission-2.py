class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_in_s = {}
        if len(s)!=len(t): return False
        for letter in s:
            if letter not in seen_in_s:
                # first time seeing it
                seen_in_s[letter] = 1
            else:
                # we've seen it before
                seen_in_s[letter] += 1
        for letter in t:
            if letter in seen_in_s:

                if seen_in_s[letter]==0:
                    return False
                else:
                   seen_in_s[letter] -= 1

            else: return False
        return True