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

    def __search(self, data):
        node = self.head
        while node is not None:
            if node.data == data:
                return node
            node = node.next
        return None

    def search(self, data):
        node = self.__search(data)
        return node is not None

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


