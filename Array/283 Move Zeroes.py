"""
双指针
如果当前元素是非 0 的，那么它的正确位置最多可以是当前位置或者更早的位置。如果是后者，则当前位置最终将被非 0 或 0 占据，该非 0 或 0 位于大于 “cur” 索引的索引处。我们马上用 0 填充当前位置，这样不像以前的解决方案，我们不需要在下一个迭代中回到这里。

1.慢指针（lastnonzerofoundat）之前的所有元素都是非零的。
2.当前指针和慢速指针之间的所有元素都是零。

当我们遇到一个非零元素时，我们需要<交换>当前指针和慢速指针指向的元素，然后前进两个指针。如果它是零元素，我们只前进当前指针。
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1