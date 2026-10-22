class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for el in strs:
            sorted_str = ''.join(sorted(el))  # questo penso sia un'inefficienza perché in python str sono immutabili, però in questo caso avevo pensato di farlo cosi, quindi si aumenta la memoria
            if sorted_str in hm:
                hm[sorted_str].append(el)  # è già una lista, quindi si può appendere
            else:
                hm[sorted_str] = [el]  # è il primo valore, però appunto deve essere strutturato come lista per il ramo if
        return list(hm.values())
        