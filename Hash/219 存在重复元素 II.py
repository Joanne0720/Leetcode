"""
需要大小为k的滑动窗口，想到队列
需要一个支持在常量时间内完成 搜索，删除，插入 操作的数据结构，那就是散列表。
"""


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 大小为k的散列表
        window = set()
        for i in range(len(nums)):
            if nums[i] in window:
                return True
            else:
                window.add(nums[i])
            if len(window) > k:
                window.remove(nums[i-k])
        return False