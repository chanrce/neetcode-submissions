class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # make the two pointers
        # w for word and a for abbr
        w=0
        a=0
        while a<len(abbr):
            #if 0 return false
            if abbr[a]=="0":
                return False
            # else keep reading digits til you hit letter or end
            else:
                if abbr[a].isalpha():
                    if w>=len(word):
                        return False
                    if word[w]!=abbr[a]:
                        return False
                    a+=1
                    w+=1 
            #convert whole thing to integer
                # while abbr end is not reached and char is digit
                else:
                    sublen=0
                    while a<len(abbr) and abbr[a].isdigit():
                        sublen=sublen*10+int(abbr[a])
                        a+=1
                    w+=sublen
        return w==len(word)

            


    
