class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 注意有一个dummy head作为链表头
        self.head = Node(0)

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0: return -1
        cur = self.head
        for _ in range(index+1):
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
        new.next = self.head.next
        self.head.next = new

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new = Node(val)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        new = Node(val)
        cur = self.head
        for i in range(index):
            if cur.next:
                cur = cur.next
            else:
                return
        # 可能是加在最后
        if cur.next:
            new.next = cur.next
        cur.next = new

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0: return
        cur = self.head
        for _ in range(index):
            if cur.next:
                cur = cur.next
            else:
                return
        if cur.next:
            cur.next = cur.next.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)