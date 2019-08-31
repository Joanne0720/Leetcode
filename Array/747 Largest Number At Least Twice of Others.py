class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest, second = max(nums[0], nums[1]), min(nums[0], nums[1])
        for i in range(2, len(nums)):
            if nums[i] > largest:
                second = largest
                largest = nums[i]
            elif nums[i] > second:
                second = nums[i]
        return largest > second * 2