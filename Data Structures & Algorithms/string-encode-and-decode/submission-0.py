class Solution:

    def encode(self, strs: List[str]) -> str:
        stringona = "" 
        for s in strs:  # O(n) con n caratteri totali
            stringona += str(len(s)) + "#" + s
        return stringona   


    def decode(self, s: str) -> List[str]:
        i = 0
        strs = []
        while i < len(s):
            j = i
            while s[j] != "#":  # O(n)
                j+=1
            length = int(s[i:j])
            start = j + 1 # non è j, perché j sarà il #
            word = s[start : start + length]
            strs.append(word)
            i = start + length
        return strs


            



