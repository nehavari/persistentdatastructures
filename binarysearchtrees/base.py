from lists.stack import Stack


class NodePreorderIterator(object):

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


class NodeInorderIterator(object):

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


class Node(object):

    __slots__ = ('left', 'value', 'right', 'parent', 'iterator')

    def __init__(self, value, left=None, right=None, iterator=None):
        self.left = left
        self.value = value
        self.right = right
        self.iterator = iterator

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

    def __copy__(self):
        return Node(
            self.value, left=self.left, right=self.right, iterator=self.iterator
        )

    def __iter__(self):
        if self.iterator == 'inorder':
            return NodeInorderIterator(self)
        else:
            return NodePreorderIterator(self)

    def __eq__(self, other):
        if self.value == other.value:
            if not self.left and not self.left or self.left and other.left and self.left == other.left:
                if not self.right and not self.right or self.right and other.right and self.right == other.right:
                    return True
        return False


class BinaryTreePreorderIterator(object):

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


class BinaryTreeInorderIterator(object):

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
