from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [*(Counter(nums1) & Counter(nums2)).elements()]
        # 对于两个 Counter 对象，与操作意味着取两者都有的key, value取小的那一个

"""
哈希表法：
首先统计数组1中所有元素的出现次数<元素,出现次数>
然后再遍历数组2，如果数组2中的元素在map中存在（出现次数大于0），就将其存入返回数组中并且将map中该元素的出现次数减一.

先排序法：
双指针 or 二分查找
"""