"""
哈希表加堆排序
为什么用堆排序？
堆排序处理海量数据的topK，分位数非常合适，因为它不用将所有的元素都进行排序，只需要比较和根节点的大小关系就可以了，同时也不需要一次性将所有的数据都加载到内存。
维护一个元素数目为 k 的最小堆,每次都将新的元素与堆顶元素（堆中频率最小的元素）进行比较,如果新的元素的频率比堆顶端的元素大，则弹出堆顶端的元素，将新的元素添加进堆
"""
import collections
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)
    # heapq.nlargest(n, iterable[, key])
    # Return a list with the n largest elements from the dataset defined by iterable.
    # key, if provided, specifies a function of one argument that is used to extract a comparison key from each element in the iterable

# 一行：   return [i[0] for i in Counter(nums).most_common(k)]