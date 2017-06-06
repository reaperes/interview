import unittest
from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.list = LinkedList()

    def test_is_empty(self):
        self.assertTrue(self.list.is_empty())

        self.list.add(1)
        self.assertFalse(self.list.is_empty())

    def test_length(self):
        self.assertIs(0, self.list.length)

        self.list.add(1)
        self.assertIs(1, self.list.length)

    def test_add(self):
        self.list.add(0)
        self.list.add(1)
        self.list.add(2)
        self.assertIs(3, self.list.length)

    def test_search(self):
        self.list.add(0)
        self.assertTrue(self.list.search(0))
        self.assertFalse(self.list.search(1))

    def test_remove(self):
        self.list.add(0)
        self.list.add(1)
        self.list.add(2)
        self.assertIs(3, self.list.length)

        self.list.remove(999)
        self.assertIs(3, self.list.length)

        self.list.remove(2)
        self.list.remove(1)
        self.assertIs(1, self.list.length)
