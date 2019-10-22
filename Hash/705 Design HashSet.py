"""
用一段有限数组(size)作为容器(bucket)，使用哈希函数（这里为key%size）算出该数字该放的位置。
若已有数字在内（即发生冲突）
在存储数据的过程中，如果发生冲突，可以利用链表在已有数据的后面插入新数据 来解决冲突。这种方法被称为“链地址法”
"""

class Node:

    def __init__(self, val, node):
        self.val = val
        self.next = node

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        # 设置dummy head，而不是空数组
        self.buckets = [Node(None, None) for _ in range(self.size)]

    def add(self, key: int) -> None:
        new = Node(key, None)
        prev = self.buckets[key % self.size]
        cur = prev.next
        while cur:
            if cur.val == key:
                break
            prev = cur
            cur = cur.next
        # 为什么这里加else：如果是通过break跳出循环则不用执行，可以省略判断if cur is None
        else:
            prev.next = new

    def remove(self, key: int) -> None:
        prev = self.buckets[key % self.size]
        cur = prev.next
        while cur:
            if cur.val == key:
                prev.next = cur.next
                break
            prev, cur = cur, cur.next

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        cur = self.buckets[key % self.size]
        while cur:
            if cur.val == key:
                return True
            cur = cur.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)