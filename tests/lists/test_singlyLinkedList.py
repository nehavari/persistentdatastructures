from unittest import TestCase
from lists.singlylinkedlist import SinglyLinkedList
import unittest


class TestSinglyLinkedList(TestCase):

    def test_append(self):
        list1 = SinglyLinkedList(1)
        list1.append(2)
        list1.append(3)
        self.assertEqual(list(list1), [1, 2, 3])

    def test_appendanotherlist(self):
        list1 = SinglyLinkedList(1)
        list1.append(2)
        list1.append(3)

        list2 = SinglyLinkedList(4)
        list2.append(5)
        list2.append(6)

        list1.append(list2)

        i = 0

        for l in list1:
            if i == 0:
                self.assertEqual(l, 1)
            if i == 3:
                self.assertEqual(list(l), [4, 5, 6])
            i += 1

        self.assertEqual(list(list1), [1, 2, 3, [4, 5, 6]])

    def test_appendlist(self):
        """
        persistent test
        :return:
        """
        list1 = SinglyLinkedList(1)
        list1.append(2)
        list1.append(3)

        list2 = SinglyLinkedList(4)
        list2.append(5)
        list2.append(6)

        list3 = list1.appendlist(list2)

        self.assertEqual(list(list1), [1, 2, 3])
        self.assertEqual(list(list2), [4, 5, 6])
        self.assertEqual(list(list3), [1, 2, 3, 4, 5, 6])


if __name__ == '__main__':
    unittest.main()
