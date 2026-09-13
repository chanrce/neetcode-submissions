class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # defaultdict(list) makes an empty list whenever a new key is accessed
        res = defaultdict(list)
        for s in strs:
            # one slot in list for every lowercase letter ie [0,0,0,0,0,0, etc]
            count = [0] * 26
            for c in s:
                # subtract a bc we want each letter to correspond to 1 position in our list, ie a should be index 0, z index 25
                count[ord(c) - ord('a')] += 1
            #lists can't be dict key bc they are mutable, but tuples can bc they are immutable
            res[tuple(count)].append(s)
        return list(res.values())