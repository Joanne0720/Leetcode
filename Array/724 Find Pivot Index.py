class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        s1 = 0
        for i in range(len(nums)):
            if s1 == (s - nums[i]) / 2:
                return i
            s1 = s1 + nums[i]
        return -1
