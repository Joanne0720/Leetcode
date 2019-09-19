#class Solution:
#    def rotate(self, nums: List[int], k: int) -> None:
#        """
#        Do not return anything, modify nums in-place instead.
#        """
#        n = len(nums)
#        k %= n
#        nums[:] = nums[-k:] + nums[:-k]

# 方法二：反转三次
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
            Do not return anything, modify nums in-place instead.
            """
        n = len(nums)
        k %= n
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
