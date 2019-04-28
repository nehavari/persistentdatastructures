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

    def test_appendlistOneElement(self):
        """
        persistent test
        :return:
        """
        list1 = SinglyLinkedList(1)

        list2 = SinglyLinkedList(4)
        list2.append(5)
        list2.append(6)

        list3 = list1.appendlist(list2)

        self.assertEqual(list(list1), [1])
        self.assertEqual(list(list2), [4, 5, 6])
        self.assertEqual(list(list3), [1, 4, 5, 6])

    def test_appendlistList2None(self):
        """
        persistent test
        :return:
        """
        list1 = SinglyLinkedList(1)

        list2 = None

        list3 = list1.appendlist(list2)

        self.assertEqual(list(list1), [1])
        self.assertEqual(list2, None)
        self.assertEqual(list(list3), [1])

    def test_suffixes(self):
        mylist = SinglyLinkedList(1)
        mylist.append(2)
        mylist.append(3)
        mylist.append(4)

        suffiexeslist = mylist.suffixes()

        self.assertEqual(list(suffiexeslist), [[1, 2, 3, 4], [2, 3, 4], [3, 4], [4], []])

    def test_iterationdepth(self):
        mylist = SinglyLinkedList(1)
        mylist.append(SinglyLinkedList(2))
        third = SinglyLinkedList(3)
        third.append(SinglyLinkedList(4))
        mylist.append(third)

        self.assertEqual(list(mylist), [1, [2], [3, [4]]])

    def test_update(self):
        mylist = SinglyLinkedList(1)
        mylist.append(2)
        mylist.append(3)
        mylist.append(4)

        newList = mylist.update(2, 7)

        self.assertEqual(list(mylist), [1, 2, 3, 4])
        self.assertEqual(list(newList), [1, 7, 3, 4])

if __name__ == '__main__':
    unittest.main()
