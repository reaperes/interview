class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def search(self, data):
        node = self.head
        while node is not None:
            if node.data == data:
                return True
            node = node.next
        return False

    @property
    def length(self):
        count = 0
        node = self.head

        while node is not None:
            count += 1
            node = node.next

        return count

    def print(self):
        node = self.head
        while node is not None:
            print(node.data + ' ')
            node = node.next


linked_list = LinkedList()
assert linked_list.is_empty() is True
assert linked_list.length is 0

linked_list.add(1)
assert linked_list.length is 1

linked_list.add(2)
linked_list.add(3)
linked_list.add(4)
assert linked_list.length is 4
assert linked_list.search(4) is True
assert linked_list.search(5) is False

