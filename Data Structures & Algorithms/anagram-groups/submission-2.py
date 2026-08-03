class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # for each word:
    # sort the letters
    # use the sorted word as the key
    # append the original word to groups[key]

#return all the values in groups
        groups = {}
        for word in strs:
            sortedS="".join(sorted(word))
            if sortedS in groups:
                groups[sortedS].append(word)
            else:
                groups[sortedS]=[word]
        answer = list(groups.values())
        return answer