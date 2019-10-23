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