from unittest import TestCase
from binarysearchtrees.unbalancedset import UnbalancedSet, _Node
from binarysearchtrees.utils import height
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
            balanceFactor.append(height(node))
        self.assertEqual(balanceFactor, [1, 2, 1, 4, 3, 2, 1])

    def test_calculate_balance_factor_all_right_nodes(self):
        set = UnbalancedSet(55).insert(56).insert(57).insert(58).insert(59)
        balanceFactors = []
        for node in set._UnbalancedSet__root:
            balanceFactors.append(height(node))
        self.assertEqual(balanceFactors, [5, 4, 3, 2, 1])

    def test_calculate_balance_factor_all_left_nodes(self):
        set = UnbalancedSet(55).insert(54).insert(53).insert(52).insert(51)
        balanceFactors = []
        node_values = []
        for node in set._UnbalancedSet__root:
            node_values.append(node.value)
            balanceFactors.append(height(node))
        self.assertEqual(balanceFactors, [1, 2, 3, 4, 5])
        self.assertEqual(node_values, [51, 52, 53, 54, 55])

    def test_calculate_balance_factor_all_left_node_one_right(self):
        set = UnbalancedSet(55).insert(54).insert(53).insert(52).insert(51).insert(59)
        balanceFactors = []
        node_values = []
        for node in set._UnbalancedSet__root:
            node_values.append(node.value)
            balanceFactors.append(height(node))
        self.assertEqual(balanceFactors, [1, 2, 3, 4, 5, 1])
        self.assertEqual(node_values, [51, 52, 53, 54, 55, 59])

    def test_calculate_balance_factor_all_right_nodes_one_left(self):
        set = UnbalancedSet(55).insert(56).insert(57).insert(58).insert(59).insert(51)
        balanceFactors = []
        for node in set._UnbalancedSet__root:
            balanceFactors.append(height(node))
        self.assertEqual(balanceFactors, [1, 5, 4, 3, 2, 1])

    def test_calculate_balance_2(self):
        set = UnbalancedSet(55).insert(56).insert(57).insert(58).insert(59).insert(51).insert(50).insert(49)
        height1 = []
        for node in set._UnbalancedSet__root:
            height1.append(height(node))
        self.assertEqual(height1, [1, 2, 3, 5, 4, 3, 2, 1])

    def test_preorder_iteration(self):
        set = UnbalancedSet(55, iterator='preorder').insert(56).insert(57).insert(58).insert(59).insert(51).insert(50)
        set = set.insert(49)
        self.assertEqual(set, [55, 51, 50, 49, 56, 57, 58, 59])

    def test2_preorder_iteration(self):
        set = UnbalancedSet(45, iterator='preorder').insert(44).insert(46).insert(48).insert(47).insert(41).insert(50)
        set = set.insert(49)
        self.assertEqual(set, [45, 44, 41, 46, 48, 47, 50, 49])

    def test3_preorder_iteration_and_height(self):
        set = UnbalancedSet(30, iterator='preorder').insert(10).insert(20)
        self.assertEqual(set, [30, 10, 20])
        height1 = []
        for node in set._UnbalancedSet__root:
            height1.append(height(node))
        self.assertEqual(height1, [3, 2, 1])

    def test_balancer_right_rotation(self):
        unbalancedSet = UnbalancedSet(5, iterator='preorder').insert(4).insert(3)
        balancedSet = unbalancedSet.balancer()
        self.assertEqual(unbalancedSet, [5, 4, 3])
        self.assertEqual(balancedSet, [4, 3, 5])

    def test_balancer_left_rotation(self):
        set = UnbalancedSet(5, iterator='preorder').insert(6).insert(7)
        balancedSet = set.balancer()
        self.assertEqual(set, [5, 6, 7])
        self.assertEqual(balancedSet, [6, 5, 7])

    def test_balancer_left_right_rotation(self):
        unbalancedSet = UnbalancedSet(5, iterator='preorder').insert(4).insert(3).insert(3.5).insert(3.6).insert(6)
        balancedSet = unbalancedSet.balancer()
        self.assertEqual(unbalancedSet, [5, 4, 3, 3.5, 3.6, 6])
        self.assertEqual(balancedSet, [3.6, 3.5, 3, 5, 4, 6])

    def test_balancer_left_right_rotation1(self):
        set = UnbalancedSet(11, iterator='preorder').insert(8).insert(13).insert(9).insert(4).insert(1).insert(2)
        set = set.insert(3).insert(12).insert(14)
        balancedSet = set.balancer()
        self.assertEqual(set, [11, 8, 4, 1, 2, 3, 9, 13, 12, 14])
        self.assertEqual(balancedSet, [8, 2, 1, 3, 4, 13, 11, 9, 12, 14])

    def test_balancer_left_right_rotation2(self):
        set = UnbalancedSet(55, iterator='preorder').insert(54).insert(53).insert(52).insert(56).insert(57).insert(58)
        balancedSet = set.balancer()
        self.assertEqual(set, [55, 54, 53, 52, 56, 57, 58])
        self.assertEqual(balancedSet, [55, 53, 52, 54, 57, 56, 58])

    def test_balancer_left_right_rotation3(self):
        set = UnbalancedSet(55, iterator='preorder').insert(54).insert(53).insert(56).insert(57).insert(58)
        balancedSet = set.balancer()
        self.assertEqual(set, [55, 54, 53, 56, 57, 58])
        self.assertEqual(balancedSet, [55, 54, 53, 57, 56, 58])

    def test_self_balancing_insert_right_rotation(self):
        set1 = UnbalancedSet(55, iterator='preorder')
        set2 = set1.bInsert(54)
        set3 = set2.bInsert(53)
        self.assertEqual(set1, [55])
        self.assertEqual(set2, [55, 54])
        self.assertEqual(set3, [54, 53, 55])

    def test_self_balancing_insert_left_rotation(self):
        set1 = UnbalancedSet(55, iterator='preorder')
        set2 = set1.bInsert(56)
        set3 = set2.bInsert(57)
        self.assertEqual(set1, [55])
        self.assertEqual(set2, [55, 56])
        self.assertEqual(set3, [56, 55, 57])

    def test_self_balancing_insert_left_right_rotation(self):
        set1 = UnbalancedSet(55, iterator='preorder')
        set2 = set1.bInsert(56)
        set3 = set2.bInsert(57).bInsert(54).bInsert(58).bInsert(59).bInsert(53)
        self.assertEqual(set1, [55])
        self.assertEqual(set2, [55, 56])
        self.assertEqual(set3, [56, 54, 53, 55, 58, 57, 59])

    def test_self_balancing_insert_left_right_rotation1(self):
        set = UnbalancedSet(11, iterator='preorder').bInsert(8).bInsert(13).bInsert(9).bInsert(4)
        self.assertEqual(set, [11, 8, 4, 9, 13])
        set = set.bInsert(1)
        self.assertEqual(set, [8, 4, 1, 11, 9, 13])
        set = set.bInsert(2)
        set = set.bInsert(3).bInsert(12).bInsert(14)
        self.assertEqual(set, [8, 2, 1, 4, 3, 11, 9, 13, 12, 14] )


if __name__ == '__main__':
    unittest.main()