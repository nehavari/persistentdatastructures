from unittest import TestCase
from binarysearchtrees.unbalancedset import UnbalancedSet, _Node
import unittest


class TestUnbalancedSet(TestCase):

    def test__insert(self):
        set = UnbalancedSet()
        set.insert(5)
        self.assertEqual(set, [5])

        set = set.insert(4)
        self.assertEqual(set, [4, 5])

        set = set.insert(8)
        self.assertEqual(set, [4, 5, 8])

        set = set.insert(3)
        set = set.insert(6)
        self.assertEqual(set, [3, 4, 5, 6, 8])

    def test_is_member(self):
        set = UnbalancedSet().insert(5).insert(4).insert(8).insert(3).insert(6)
        self.assertTrue(set.is_member(3))
        self.assertFalse(set.is_member(10))

    def test_insert_for_immutability(self):
        set = UnbalancedSet(10)
        set1 = set.insert(2)
        set2 = set.insert(8)
        set3 = set2.insert(2)

        self.assertEqual(set, [10])
        self.assertEqual(set1, [2, 10])
        self.assertEqual(set2, [8, 10])
        self.assertEqual(set3, [2, 8, 10])

    def test_insert_for_sharing(self):
        set = UnbalancedSet('d').insert('b').insert('g').insert('h').insert('f').insert('a').insert('c')
        self.assertEqual(set, ['a', 'b', 'c', 'd', 'f', 'g', 'h'])

        set1 = set.insert('e')
        self.assertEqual(set, ['a', 'b', 'c', 'd', 'f', 'g', 'h'])

        self.assertEqual(set1, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

    def test_existing_member(self):
        set = UnbalancedSet(1).insert(1)

        self.assertEqual(set, [1])

    def test_assign_height(self):
        set = UnbalancedSet(9).insert(5).insert(1).insert(6).insert(10)
        set = set.insert(11).insert(13)
        for node in set._UnbalancedSet__root:
            print(node, node.height)


if __name__ == '__main__':
    unittest.main()