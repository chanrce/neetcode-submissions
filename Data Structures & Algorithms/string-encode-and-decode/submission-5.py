class Solution: 
 
    def encode(self, strs: List[str]) -> str: 
        res = "" 
        for s in strs: 
            res += str(len(s)) + "#" + s 
        return res 

    def decode(self, s: str) -> List[str]: 
        decoded_strs = []
        index = 0

        while index < len(s):
            num = ""

            while s[index] != "#":
                num += s[index]
                index += 1

            count = int(num)

            index += 1

            decoded_str = ""

            while count != 0:
                decoded_str += s[index]
                index += 1
                count -= 1

            decoded_strs.append(decoded_str)

        return decoded_strs