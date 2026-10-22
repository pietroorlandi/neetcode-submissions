class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        el = 1
        for i in range(1, n):  # creo l'analogo di L
            res[i] = res[i-1] * nums[i-1]
        for j in range(n-2, -1, -1):
            el = el * nums[j+1]  # creo il valore analogo a R temporaneo
            res[j] = res[j] * el
        return res
        