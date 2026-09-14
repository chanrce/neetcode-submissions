class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        #go through each str
        for string in strs:
            count = [0]*26
            #go through each letter of each str
            for letter in string:
                count[ord(letter)-ord('a')]+=1
            res[tuple(count)].append(string)
        return list(res.values())