class Solution:

    def encode(self, strs: List[str]) -> str:
        # create an empty string to build the encoded string
        encoded = ""
        # for each string in strs
        for string in strs:
            # get the length of the string
            length=len(string)
            # add the length, then #, then the string itself
            encoded=encoded+str(length)+"#"+string
        # return the final encoded string
        return encoded


    def decode(self, s: str) -> List[str]:
        # create an empty list to store decoded strings
        store=[]
        # start at the beginning of the encoded string
        i=0
        # keep going until we reach the end of the encoded string
        while i<len(s):
            # create another pointer starting at the same position as i
            j=i
            # move that pointer until it finds #
            while s[j]!="#":
                j+=1
            # get the integer length before the #
            length = int(s[i:j])
            # grab that many characters after the # and add them to result
            store.append(s[j + 1 : j + 1 + length])
            # move i to the beginning of the next length
            i = j + 1 + length
        # return the decoded list
        return store