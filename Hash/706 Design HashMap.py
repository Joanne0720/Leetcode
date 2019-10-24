"""
哈希表原理：

Hash，一般翻译做“散列”，也有直接音译为“哈希”的，就是把任意长度的输入（又叫做预映射， pre-image），通过散列算法，变换成固定长度的输出，该输出就是散列值。
这种转换是一种压缩映射，也就是，散列值的空间通常远小于输入的空间，不同的输入可能会散列成相同的输出，而不可能从散列值来唯一的确定输入值。

简单的说就是一种将任意长度的消息压缩到某一固定长度的消息摘要的函数。

数组的特点是：寻址容易，插入和删除困难；而链表的特点是：寻址困难，插入和删除容易。

那么我们能不能综合两者的特性，做出一种寻址容易，插入删除也容易的数据结构？

答案是肯定的，这就是我们要提起的哈希表，哈希表有多种不同的实现方法，下面是最常用的一种方法——拉链法，我们可以理解为“链表的数组”。
"""


class Node:

    def __init__(self, key, value, node):
        self.key = key
        self.val = value
        self.next = node


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        # 设置dummy head，而不是空数组
        self.buckets = [Node(None, None, None) for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        prev = self.buckets[key % self.size]
        cur = prev.next
        while cur:
            if cur.key == key:
                cur.val = value
                break
            prev = cur
            cur = cur.next
        else:
            prev.next = Node(key, value, None)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        cur = self.buckets[key % self.size]
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        prev = self.buckets[key % self.size]
        cur = prev.next
        while cur:
            if cur.key == key:
                prev.next = cur.next
                break
            prev, cur = cur, cur.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)