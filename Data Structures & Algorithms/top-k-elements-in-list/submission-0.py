class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            hm[nums[i]] = hm.get(nums[i], 1) + 1
        
        # penso che alla fine di questo for dovrebbe uscire un contatore che restituisce la forma canonica
        sorted_hm = dict(sorted(hm.items(), key=lambda item: item[1], reverse=True))  # O(nlogn), con space complexity O(n)
        return list(sorted_hm.keys())[0:k]

