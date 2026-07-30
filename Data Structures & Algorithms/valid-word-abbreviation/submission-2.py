class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # define pointers
        w=0
        a=0
        while w<len(word) and a<len(abbr):
            if word[w]==abbr[a]:
                w+=1
                a+=1
            elif abbr[a]=="0":
                return False
            elif abbr[a].isdigit():
                num=0
                while a<len(abbr) and abbr[a].isdigit():
                    num=num*10+int(abbr[a])
                    a+=1
                #move pointer from w same as amt a moved
                w+=num
            # letters do not equal
            else:
                return False
        return w == len(word) and a == len(abbr)