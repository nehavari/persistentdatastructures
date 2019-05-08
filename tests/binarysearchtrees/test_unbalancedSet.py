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

    def test_calculate_balance_factor(self):
        set = UnbalancedSet(9).insert(5).insert(1).insert(6).insert(10)
        set = set.insert(11).insert(13)
        balanceFactor = []
        for node in set._UnbalancedSet__root:
            balanceFactor.append(node.height)
        self.assertEqual(balanceFactor, [1, 2, 1, 4, 3, 2, 1])

    def test_calculate_balance_factor_all_right_nodes(self):
        set = UnbalancedSet(55).insert(56).insert(57).insert(58).insert(59)
        balanceFactors = []
        for node in set._UnbalancedSet__root:
            balanceFactors.append(node.height)
        self.assertEqual(balanceFactors, [5, 4, 3, 2, 1])

    def test_calculate_balance_factor_all_left_nodes(self):
        set = UnbalancedSet(55).insert(54).insert(53).insert(52).insert(51)
        balanceFactors = []
        node_values = []
        for node in set._UnbalancedSet__root:
            node_values.append(node.value)
            balanceFactors.append(node.height)
        self.assertEqual(balanceFactors, [1, 2, 3, 4, 5])
        self.assertEqual(node_values, [51, 52, 53, 54, 55])

    def test_calculate_balance_factor_all_left_node_one_right(self):
        set = UnbalancedSet(55).insert(54).insert(53).insert(52).insert(51).insert(59)
        balanceFactors = []
        node_values = []
        for node in set._UnbalancedSet__root:
            node_values.append(node.value)
            balanceFactors.append(node.height)
        self.assertEqual(balanceFactors, [1, 2, 3, 4, 5, 1])
        self.assertEqual(node_values, [51, 52, 53, 54, 55, 59])

    def test_calculate_balance_factor_all_right_nodes_one_left(self):
        set = UnbalancedSet(55).insert(56).insert(57).insert(58).insert(59).insert(51)
        balanceFactors = []
        for node in set._UnbalancedSet__root:
            balanceFactors.append(node.height)
        self.assertEqual(balanceFactors, [1, 5, 4, 3, 2, 1])

    def test_calculate_balance_2(self):
        set = UnbalancedSet(55).insert(56).insert(57).insert(58).insert(59).insert(51).insert(50).insert(49)
        balanceFactors = []
        for node in set._UnbalancedSet__root:
            balanceFactors.append(node.height)
        self.assertEqual(balanceFactors, [1, 2, 3, 5, 4, 3, 2, 1])


if __name__ == '__main__':
    unittest.main()