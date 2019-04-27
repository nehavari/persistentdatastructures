class _NodeIterator(object):

    def __init__(self, node):
        self._node = node

    def __iter__(self):
        return self

    def __next__(self):
        if not self._node:
            raise StopIteration()
        currentNode = self._node
        self._node = self._node.getNextNode()
        return currentNode


class _Node(object):

    def __init__(self, value, next=None):
        self._value = value
        self._next = next

    def getValue(self):
        return self._value

    def getNextNode(self):
        return self._next

    def setNextNode(self, node):
        self._next = node

    def __iter__(self):
        return _NodeIterator(self)

    def __str__(self):
        return str(self._value)


class _SinglyLinkedListIterator(object):

    def __init__(self, list):
        self.pointer = list

    def __iter__(self):
        return self

    def __next__(self):
        if not self.pointer:
            raise StopIteration()

        currentValue = self.pointer.getValue()
        self.pointer = self.pointer.getNextNode()

        if isinstance(currentValue, SinglyLinkedList):
            currentValue = list(currentValue)

        return currentValue


class SinglyLinkedList(object):

    def __init__(self, value):
        self.head = _Node(value)

    def append(self, value):
        lastNode = None

        for h in self.head:
            lastNode = h

        lastNode.setNextNode(_Node(value))

    def appendlist(self, anotherlist):
        '''
        persistent implementation of concatenation of 2 lists
        Catenating two lists
        fig 2.5 of the book "purely functional data structures" by Chris Okasaki
        :param anotherList:
        :return: third list which has values of both the list
        '''

        if not anotherlist:
            return self

        newlist = SinglyLinkedList(self.head.getValue())
        pointer = newlist.head

        if self.head.getNextNode():
            for h in self.head.getNextNode():
                pointer.setNextNode(_Node(h.getValue()))
                pointer = pointer.getNextNode()

        pointer.setNextNode(anotherlist.head)

        return newlist

    def __iter__(self):
        return _SinglyLinkedListIterator(self.head)

