class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            # skip non-alphanumeric on left
            if not s[i].isalnum():
                i += 1
                continue

            # skip non-alphanumeric on right
            if not s[j].isalnum():
                j -= 1
                continue

            # compare characters
            if s[i].lower() != s[j].lower():
               return False

            # move both pointers inward
            i += 1
            j -= 1

        return True
