from unittest import TestCase
from lists.singlylinkedlist import SinglyLinkedList
import unittest


class TestSinglyLinkedList(TestCase):

    def test_append(self):
        list1 = SinglyLinkedList(1)
        list2 = list1.append(2)
        list3 = list1.append(3)
        list4 = list3.append(3).append(4).append(5)
        self.assertEqual(list1, [1])
        self.assertEqual(list2, [1, 2])
        self.assertEqual(list3, [1, 3])
        self.assertEqual(list4, [1, 3, 3, 4, 5])

    def test_appendanotherlist(self):
        list1 = SinglyLinkedList(1).append(2).append(3)
        list2 = SinglyLinkedList(4).append(5).append(6)
        list1 = list1.append(list2)

        i = 0

        for l in list1:
            if i == 0:
                self.assertEqual(l, 1)
            if i == 3:
                self.assertEqual(l, [4, 5, 6])
            i += 1

        self.assertEqual(list1, [1, 2, 3, [4, 5, 6]])

    def test_appendlist(self):
        """
        persistent test
        :return:
        """
        list1 = SinglyLinkedList(1).append(2).append(3)

        list2 = SinglyLinkedList(4).append(5).append(6)

        list3 = list1.appendlist(list2)

        self.assertEqual(list1, [1, 2, 3])
        self.assertEqual(list2, [4, 5, 6])
        self.assertEqual(list3, [1, 2, 3, 4, 5, 6])

    def test_appendlistOneElement(self):
        """
        persistent test
        :return:
        """
        list1 = SinglyLinkedList(1)

        list2 = SinglyLinkedList(4).append(5).append(6)

        list3 = list1.appendlist(list2)

        self.assertEqual(list1, [1])
        self.assertEqual(list2, [4, 5, 6])
        self.assertEqual(list3, [1, 4, 5, 6])

    def test_appendlistList2None(self):
        """
        persistent test
        :return:
        """
        list1 = SinglyLinkedList(1)

        list2 = None

        list3 = list1.appendlist(list2)

        self.assertEqual(list1, [1])
        self.assertEqual(list2, None)
        self.assertEqual(list3, [1])

    def test_suffixes(self):
        mylist = SinglyLinkedList(1).append(2).append(3).append(4)
        suffiexeslist = mylist.suffixes()
        self.assertEqual(suffiexeslist, [[1, 2, 3, 4], [2, 3, 4], [3, 4], [4], []])

    def test_iterationdepth(self):
        mylist = SinglyLinkedList(1).append(SinglyLinkedList(2))
        third = SinglyLinkedList(3).append(SinglyLinkedList(4))
        second = mylist.append(third)

        self.assertEqual(second, [1, [2], [3, [4]]])

    def test_update(self):
        mylist = SinglyLinkedList(1).append(2).append(3).append(4)
        newList = mylist.update(2, 7)

        self.assertEqual(mylist, [1, 2, 3, 4])
        self.assertEqual(newList, [1, 7, 3, 4])

    def test_appendOneElement(self):
        slist = SinglyLinkedList(1).append(2)
        self.assertEqual(slist, [1, 2])

    def test_iterateAListOfOneElement(self):
        slist = SinglyLinkedList(1)
        for l in slist:
            self.assertEqual(l, 1)

    def test_iterateAListOfOneList(self):
        slist = SinglyLinkedList(SinglyLinkedList(1))
        for l in slist:
            self.assertEqual(l, [1])

    def test_iterateAListOfOneList1(self):
        slist = SinglyLinkedList(SinglyLinkedList(1).append(2))
        for l in slist:
            self.assertEqual(l, [1, 2])

    def test_iterateAListOfOneList2(self):
        slist = SinglyLinkedList(SinglyLinkedList(1).append(2)).append(8)
        self.assertEqual(slist, [[1, 2], 8])



if __name__ == '__main__':
    unittest.main()
