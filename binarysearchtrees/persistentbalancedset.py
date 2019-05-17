'''
    A persistent balanced set implemented using binary search tree
'''

from lists.stack import Stack
from copy import copy
from binarysearchtrees.utils import getBalanceFactor, isBalancedTree
from binarysearchtrees.base import Node, BinaryTreeInorderIterator, BinaryTreePreorderIterator


class PersistentBalancedSet(object):

    __slots__ = ('__root', '_iterator')

    def __init__(self, root_val=None, iterator='inorder'):
        if root_val:
            object.__setattr__(self, '_PersistentBalancedSet__root', Node(root_val, iterator=iterator))
        else:
            object.__setattr__(self, '_PersistentBalancedSet__root', None)
        self._iterator = iterator

    def __len__(self):
        length = 0
        if not self.__root:
            return length
        for node in self.__root:
            length += 1
        return length

    def _value_for_str(self, value):
        if isinstance(value, str):
            return "'"+value+"'"
        return str(value)

    def __str__(self):
        args = '['
        if len(self) == 0:
            args += ''
        else:
            for node in self.__root:
                args += self._value_for_str(node.value) + ', '

            args = args[:-2]

        args += ']'

        return args

    def __repr__(self):
        args = '['
        if len(self) == 0:
            args += ''
        else:
            for node in self.__root:
                args += self._value_for_str(node.value) + ', '

            args = args[:-2]

        args += ']'

        return args

    def __eq__(self, other):
        if len(self) != len(other):
            return False

        for valueSelf, valueOther in zip(self, other):
            if valueSelf != valueOther:
                return False
        return True

    def __iter__(self):
        if self._iterator == 'inorder':
            return BinaryTreeInorderIterator(self.__root)
        else:
            return BinaryTreePreorderIterator(self.__root)

    def _insertNode(self, node, elementNode):
        if elementNode.value < node.value:
            if node.left:
                cnode = copy(node.left)
                node.left = cnode
                self._insertNode(cnode, elementNode)
            else:
                node.left = elementNode

        elif elementNode.value > node.value:
            if node.right:
                cnode = copy(node.right)
                node.right = cnode
                self._insertNode(cnode, elementNode)
            else:
                node.right = elementNode

    def isMember(self, value):
        for node in self.__root:
            if node.value == value:
                return True
        return False

    def _rightRotation(self, node, parent, set):
        if not parent:
            set.__root = node.left
        else:
            if parent.right and parent.right == node:    # check if node is right child of its parent
                parent.right = node.left
            else:
                parent.left = node.left

        pivot = node.left
        if pivot.right:
            pivot.right = copy(pivot.right)
            set._insertNode(pivot.right, Node(node.value, right=node.right))
        else:
            pivot.right = Node(node.value, right=node.right)

    def _leftRotation(self, node, parent, set):
        if not parent:
            set.__root = node.right
        else:
            if parent.right and parent.right == node:   # check if node is right child of its parent
                parent.right = node.right
            else:
                parent.left = node.right

        pivot = node.right
        if pivot.left:
            pivot.left = copy(pivot.left)
            set._insertNode(pivot.left, Node(node.value, left=node.left))
        else:
            pivot.left = Node(node.value, left=node.left)

    def _balance(self, root):

        # balancer will always produce a new balanced set
        balancedSet = PersistentBalancedSet(iterator=self._iterator)
        rightStack = Stack()

        # last default values for first iteration
        lastBalanceFactor = 0
        lastNode = None
        lastParent = None

        # current default values for first iteration
        parent = None  # for root parent will be None
        node = root.__root
        isUnbalanced = False

        while node:
            balanceFactor = getBalanceFactor(node)
            if balanceFactor < -1 or balanceFactor > 1:
                isUnbalanced = True
            if isUnbalanced and balanceFactor in (1, 0, -1):
                if lastBalanceFactor < -1:
                    self._rightRotation(lastNode, lastParent, balancedSet)
                else:
                    self._leftRotation(lastNode, lastParent, balancedSet)
                return balancedSet

            if not balancedSet.__root:
                node = copy(node)
                object.__setattr__(balancedSet, '_PersistentBalancedSet__root', node)

            # WARNING: change order of execution of below section on your own risk.
            if node.right:
                rnode = copy(node.right)
                node.right = rnode
                rightStack.push((rnode, node,))  # a tuple of right node and its parent, preserving right elements

            if node.left:
                lnode = copy(node.left)
                node.left = lnode

            # useful for next iteration
            lastNode = node
            lastParent = parent
            lastBalanceFactor = balanceFactor

            # this is to set next node in iteration as per preorder traversal rules
            if node.left:
                parent = node
                node = node.left
            elif not rightStack.isEmpty():
                element = rightStack.pop()
                node = element[0]
                parent = element[1]
            else:
                node = None

        return balancedSet

    def balancer(self):
        isBalanced = isBalancedTree(self.__root)
        set = self
        while not isBalanced:
            set = self._balance(set)
            isBalanced = isBalancedTree(set.__root)
        return set

    def insert(self, element):
        '''
          An insert respecting the immutability, sharing and balance factor of a set.
          A self balancing insert.
          :param element:
          :return: A new unbalanced set which copies all the nodes of orignal set along the search path and
              share rest of the nodes with the original set.
        '''
        if not self.__root:
            object.__setattr__(self, '_PersistentBalancedSet__root', Node(element, iterator=self._iterator))
        elif not self.isMember(element):
            set = PersistentBalancedSet(iterator=self._iterator)
            object.__setattr__(set, '_PersistentBalancedSet__root', copy(self.__root))
            self._insertNode(set.__root, Node(element, iterator=self._iterator))

            return set.balancer()
        return self

    def _deleteElement(self, set, element):
        parent = None
        node = set.__root
        while node:
            if node.value == element:
                if not parent:
                    if node.left:
                        object.__setattr__(set, '_PersistentBalancedSet__root', node.left)
                        if node.right:
                            if node.left.right:
                                cNode = copy(node.left.right)
                                node.left.right = cNode
                                set._insertNode(node.left.right, node.right)
                            else:
                                node.left.right = node.right
                    elif node.right:
                        object.__setattr__(set, '_PersistentBalancedSet__root', node.right)
                    else:
                        object.__setattr__(set, '_PersistentBalancedSet__root', None)  # for set of only one node
                elif parent.left and parent.left == node:  # check if node if the left child of its parent
                    if not node.right and not node.left:  # node to be deleted is a leaf node
                        parent.left = None
                    elif node.right:
                        parent.left = node.right
                        if node.left and node.right.left:
                            cNode = copy(node.right.left)
                            node.right.left = cNode
                            set._insertNode(node.right.left, node.left)
                        else:
                            node.right.left = node.left
                    else:
                        parent.left = node.left
                else:  # fall here as node is the right child of its parent
                    if not node.right and not node.left:  # node to be deleted is a leaf node
                        parent.right = None
                    elif node.right:
                        parent.right = node.right
                        if node.left and node.right.left:
                            cNode = copy(node.right.left)
                            node.right.left = cNode
                            set._insertNode(node.right.left, node.left)
                        else:
                            node.right.left = node.left
                    else:
                        parent.right = node.left
                break

            # preparations for next iteration
            parent = node

            if element < node.value:
                node = node.left
            else:
                node = node.right

            if node and node.left:
                lNode = copy(node.left)
                node.left = lNode

            if node and node.right:
                rNode = copy(node.right)
                node.right = rNode

    def delete(self, element):
        '''
          A delete respecting the immutability, sharing and balance factor of a set.
          A self balancing delete.
          :param element:
          :return: A new balanced set without the given element.
        '''
        if self.isMember(element):
            node = copy(self.__root)
            node.left = copy(self.__root.left)
            node.right = copy(self.__root.right)
            set = PersistentBalancedSet(iterator=self._iterator)
            object.__setattr__(set, '_PersistentBalancedSet__root', node)
            self._deleteElement(set, element)
            return set.balancer()
        return self

    def union(self, other):
        if not other:
            return self
        unbalanced_set = PersistentBalancedSet(iterator=self._iterator)
        object.__setattr__(unbalanced_set, '_PersistentBalancedSet__root', copy(self.__root))
        for node in other.__root:
            if not unbalanced_set.isMember(node.value):
                self._insertNode(unbalanced_set.__root, Node(node.value))
        return unbalanced_set.balancer()

    def difference(self, other):
        if not other:
            return self
        node = copy(self.__root)
        node.left = copy(self.__root.left)
        node.right = copy(self.__root.right)
        unbalanced_set = PersistentBalancedSet(iterator=self._iterator)
        object.__setattr__(unbalanced_set, '_PersistentBalancedSet__root', node)
        for node in other.__root:
            if unbalanced_set.isMember(node.value):
                self._deleteElement(unbalanced_set, node.value)
        return unbalanced_set.balancer()

    def __sub__(self, other):
        return self.difference(other)

    def __add__(self, other):
        return self.union(other)
