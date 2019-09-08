class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result, count = 0, 0
        for n in nums:
            if n:
                count += 1
            else:
                result = max(result, count)
                count = 0
        return max(result, count)