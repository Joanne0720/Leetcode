class Node(object):
    def __init__(self, x):
        self.val = x
        self.prev = None
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or self.head is None:
            return -1
        cur = self.head
        for _ in range(index):
            if cur.next:
                cur = cur.next
            else:
                return -1
        return cur.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new = Node(val)
        # 如果是空链表
        if self.head is None:
            self.head = new
            return
        self.head, new.next, self.head.prev = new, self.head, new

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new = Node(val)
        # 如果是空链表
        if self.head is None:
            self.head = new
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next, new.prev = new, cur

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index <= 0:
            self.addAtHead(val)
            return
        if self.head is None:
            return
        new = Node(val)
        pre = self.head
        for _ in range(index-1):
            if pre.next:
                pre = pre.next
            else:
                return
        if pre.next:
            pre.next, new.prev, new.next, pre.next.prev = new, pre, pre.next, new
        else:
            self.addAtTail(val)

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or self.head is None:
            return
        # 删除第一个结点
        if index == 0:
            if self.head.next:
                self.head.next.prev = None
            self.head = self.head.next
            return
        pre = self.head
        for _ in range(index-1):
            if pre.next:
                pre = pre.next
            else:
                return
        # 删除最后一个节点
        if pre.next:
            pre.next = pre.next.next
            if pre.next:
                pre.next.prev = pre

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)