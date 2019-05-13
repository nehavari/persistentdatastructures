'''
    A persistent Unbalanced Set implemented using binary search tree
'''

from lists.stack import Stack
from copy import copy


class _NodePreorderIterator(object):

    def __init__(self, node):
        self._node = node
        self._accumulator = Stack()

    def __iter__(self):
        return self

    def __next__(self):
        if self._accumulator.isEmpty() and not self._node:
            raise StopIteration()

        if self._node:
            if self._node.right:
                self._accumulator.push(self._node.right)
            node = self._node
            self._node = self._node.left
        else:
            node = self._accumulator.pop()
            if node.right:
                self._accumulator.push(node.right)
            self._node = node.left

        return node


class _NodeInorderIterator(object):

    def __init__(self, node):
        self._node = node
        self._accumulator = Stack()

    def __iter__(self):
        return self

    def __next__(self):
        if self._accumulator.isEmpty() and not self._node:
            raise StopIteration()

        if self._node:
            current = self._node
            while current:
                self._accumulator.push(current)
                current = current.left

        node = self._accumulator.pop()
        self._node = node.right

        return node


class _Node(object):

    __slots__ = ('left', 'value', 'right', 'parent', 'iterator')

    def __init__(self, value, parent=None, left=None, right=None, iterator=None):
        self.left = left
        self.value = value
        self.right = right
        self.parent = parent
        self.iterator = iterator

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

    def __copy__(self):
        ## parent is set to none in new copy , responsibility of actor to attach with a parent
        return _Node(
            self.value, left=self.left, right=self.right, iterator=self.iterator, parent=None
        )

    def __iter__(self):
        if self.iterator == 'inorder':
            return _NodeInorderIterator(self)
        else:
            return _NodePreorderIterator(self)


class _UnbalancedSetPreorderIterator(object):

    def __init__(self, node):
        self._node = node
        self._accumulator = Stack()

    def __iter__(self):
        return self

    def __next__(self):
        if self._node:
            if self._node.right:
                self._accumulator.push(self._node.right)
            node = self._node
            self._node = self._node.left
        else:
            if self._accumulator.isEmpty() and not self._node:
                raise StopIteration()
            node = self._accumulator.pop()
            if node.right:
                self._accumulator.push(node.right)
            self._node = node.left

        return node.value


class _UnbalancedSetInorderIterator(object):

    def __init__(self, node):
        self._node = node
        self._accumulator = Stack()

    def __iter__(self):
        return self

    def __next__(self):
        if self._accumulator.isEmpty() and not self._node:
            raise StopIteration()

        if self._node:
            current = self._node
            while current:
                self._accumulator.push(current)
                current = current.left

        node = self._accumulator.pop()
        self._node = node.right

        return node.value


class UnbalancedSet(object):

    __slots__ = ('__root', '_iterator')

    def __init__(self, root_val=None, iterator='inorder'):
        if root_val:
            object.__setattr__(self, '_UnbalancedSet__root', _Node(root_val, parent=None, iterator=iterator))
        else:
            object.__setattr__(self, '_UnbalancedSet__root', None)
        self._iterator = iterator

    def __len__(self):
        length = 0
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
            return _UnbalancedSetInorderIterator(self.__root)
        else:
            return _UnbalancedSetPreorderIterator(self.__root)

    def is_member(self, value):
        for node in self.__root:
            if node.value == value:
                return True
        return False

    def _insert(self, node, elementNode):
        if elementNode.value < node.value:
            if node.left:
                cnode = copy(node.left)
                node.left = cnode
                self._insert(cnode, elementNode)
            else:
                node.left = elementNode
                elementNode.parent = node
        elif elementNode.value > node.value:
            if node.right:
                cnode = copy(node.right)
                node.right = cnode
                self._insert(cnode, elementNode)
            else:
                node.right = elementNode
                elementNode.parent = node

    def insert(self, element):
        '''
        An insert respecting the immutability of set.
        Figure 2.8 of the book.
        :param element:
        :return: A new unbalanced set which copies all the nodes of orignal set along the search path and
            share rest of the nodes with the original set.
        '''
        if not self.__root:
            object.__setattr__(self, '_UnbalancedSet__root', _Node(element, parent=None, iterator=self._iterator))
        elif not self.is_member(element):
                set = UnbalancedSet(iterator=self._iterator)
                object.__setattr__(set, '_UnbalancedSet__root', copy(self.__root))
                self._insert(set.__root, _Node(element))
                return set
        return self

    def _height(self, node):
        if not node :
            return 0
        left = 0
        right = 0
        if node.left:
            left = self._height(node.left)
        if node.right:
            right = self._height(node.right)

        if left > right:
            return left + 1
        else:
            return right + 1

    def _right_rotation(self, node, set):
        if not node.parent:
            set.__root = copy(node.left)
            pivot = set.__root
        else:
            node.parent.left = copy(node.left)
            pivot = node.parent

        if pivot.right:
            set._insert(pivot.right, _Node(node.value, right=node.right))
        else:
            pivot.right = _Node(node.value, right=node.right)

    def _left_rotation(self, node, set):
        if not node.parent:
            set.__root = copy(node.right)
            pivot = set.__root
        else:
            node.parent.right = copy(node.right)
            pivot = node.parent

        if pivot.left:
            set._insert(pivot.left, _Node(node.value, left=node.left))
        else:
            pivot.left = _Node(node.value, left=node.left)

    def _balance(self, root):
        isUnbalanced = False
        lastBalanceFactor = 0
        set = UnbalancedSet(iterator='preorder')
        object.__setattr__(set, '_UnbalancedSet__root', _Node(
            root.__root.value,
            parent=root.__root.parent,
            left=root.__root.left,
            right=root.__root.right,
            iterator='preorder'
        ))
        for node in set.__root:
            balanceFactor = self._height(node.right) - self._height(node.left)
            if balanceFactor < -1 or balanceFactor > 1:
                isUnbalanced = True
            if isUnbalanced and balanceFactor in (1, 0, -1):
                if lastBalanceFactor < -1:
                    self._right_rotation(lastNode, set)
                else:
                    self._left_rotation(lastNode, set)
                return True, set
            c_node = copy(node)
            if node.parent:
                if node.parent.left == node:
                    node.parent.left = c_node
                else:
                    node.parent.right = c_node
            lastNode = c_node
            lastBalanceFactor = balanceFactor
        return False, root

    def balancer(self):
        isUnbalanced = True
        root = self
        while isUnbalanced:
            isUnbalanced, root = self._balance(root)
        return root