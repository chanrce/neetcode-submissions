class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #storing frequency of chars in current window
        count = {}
        # largest valid window length found so far
        res = 0
        #left of sliding window
        l = 0
        #largest frequency of single char seen in window
        maxf=0

        for r in range(len(s)):
            # add current character into hashmap
            count[s[r]] = 1 + count.get(s[r], 0)
            #update highest frequency
            maxf= max(maxf,count[s[r]])
            #WHILE INVALID: window length -maxf
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            #max(old best, current window size)
            res = max(res, r - l + 1)

        return res