class Solution:
    def romanToInt(self, s: str) -> int:
        # python dict is a hashmap
        numerals = {"I": 1,
                    "V":5,
                    "X":10,
                    "L":50,
                    "C":100,
                    "D":500,
                    "M":1000}
        sum=0
        for index, value in enumerate(s):
            if index!=len(s)-1 and numerals[value]<numerals[s[index+1]]: 
                sum-=numerals[value] 
            else: 
                sum+=numerals[value] 
        return sum
