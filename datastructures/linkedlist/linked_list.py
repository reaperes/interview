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

    def remove(self, data):
        node = self.head
        if node is None:
            return

        if node.data == data:
            self.head = node.next
            return

        while node.next is not None:
            if node.next.data == data:
                node.next = node.next.next
                return
            node = node.next

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


