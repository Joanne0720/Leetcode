"""
为什么用堆排序？
堆排序处理海量数据的topK，分位数非常合适，因为它不用将所有的元素都进行排序，只需要比较和根节点的大小关系就可以了，同时也不需要一次性将所有的数据都加载到内存。
"""
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = Counter(nums)

        return [i[0] for i in Counter(nums).most_common(k)]
