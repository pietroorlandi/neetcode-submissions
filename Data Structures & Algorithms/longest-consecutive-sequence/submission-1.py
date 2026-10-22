class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)  # elimino i duplicati O(N)
        best = 0
        for el in s:
            if el -1 not in s:  # è una sequenza
                cur = el
                length = 1
                while cur +1 in s:
                    cur +=1
                    length +=1
                best = max(best, length)
        return best
            