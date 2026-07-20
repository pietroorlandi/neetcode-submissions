class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # SOL 1 O(nlogn), space complexity O(1)
        # sorted(nums)   # O(nlogn)
        # l = 0
        # r = len(nums) - 1
        # while (l<r):
        #     if(nums[l] + nums[r]) < target:
        #         l += 1
        #     elif(nums[l] + nums[r]) > target:
        #         r -= 1
        #     else:
        #         return [l, r]
        # return [-1, -1]
        # SOL2 time complexity O(n), space complexity O(n)
        hm = {}
        for i in range(len(nums)):
            if target - nums[i] in hm:
                return [min(i, hm[target - nums[i]]), max(i, hm[target - nums[i]])]
            hm[nums[i]] = i
        return [-1, -1]
