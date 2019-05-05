'''
    A persistent Unbalanced Set implemented using binary search tree
'''

from lists.stack import Stack
from copy import copy


class _NodeInorderIterator(object):

    def __init__(self, node):
        self._node = node
        self._accumulator = Stack()

    def __iter__(self):
        return self

    def __next__(self):
        if self._accumulator.isEmpty() and not self._node:
            raise StopIteration

        if self._node:
            current = self._node
            while current:
                self._accumulator.push(current)
                current = current.left

        node = self._accumulator.pop()
        self._node = node.right

        return node


class _Node(object):

    __slots__ = ('left', 'value', 'right')

    def __init__(self, value, left=None, right=None):
        self.left = left
        self.value = value
        self.right = right

    def __str__(self):
        return str(self.value) + ' ' + object.__str__(self)

    def __repr__(self):
        return str(self.value)

    def __copy__(self):
        return _Node(self.value, left=self.left, right=self.right)

    def __iter__(self):
        return _NodeInorderIterator(self)


class _UnbalancedSetInorderIterator(object):

    def __init__(self, node):
        self._node = node
        self._accumulator = Stack()

    def __iter__(self):
        return self

    def __next__(self):
        if self._accumulator.isEmpty() and not self._node:
            raise StopIteration

        if self._node:
            current = self._node
            while current:
                self._accumulator.push(current)
                current = current.left

        node = self._accumulator.pop()
        self._node = node.right

        return node.value


class UnbalancedSet(object):

    __slots__ = ('__root', )

    def __init__(self, root_val=None):
        if root_val:
            object.__setattr__(self, '_UnbalancedSet__root', _Node(root_val))
        else:
            object.__setattr__(self, '_UnbalancedSet__root', None)

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
        return _UnbalancedSetInorderIterator(self.__root)

    def __setattr__(self, key, value):
        raise AttributeError('Mutating root of set not supported')

    def is_member(self, value):
        for node in self.__root:
            if node.value == value:
                return True
        return False

    def _insert(self, node, element):
        if element < node.value:
            if node.left:
                cnode = copy(node.left)
                node.left = cnode
                self._insert(cnode, element)
            else:
                node.left = _Node(element)
        elif element > node.value:
            if node.right:
                cnode = copy(node.right)
                node.right = cnode
                self._insert(cnode, element)
            else:
                node.right = _Node(element)

    def insert(self, element):
        '''
        An insert respecting the immutability of set.
        Figure 2.8 of the book.
        :param element:
        :return: A new unbalanced set which copies all the nodes of orignal set along the search path and
            share rest of the nodes with the original set.
        '''
        if not self.__root:
            object.__setattr__(self, '_UnbalancedSet__root', _Node(element))
            return self
        else:
            set = UnbalancedSet()
            object.__setattr__(set, '_UnbalancedSet__root', copy(self.__root))
            self._insert(set.__root, element)
            return set
