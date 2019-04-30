'''
SinglyLinkedList , _Node, _SinglyLinkedListIterator, _NodeIterator
'''

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

    def __str__(self):
        if self._next:
            return "Node's value is {value} with next populated".format(value=self._value)
        else:
            return "Leaf Node's value is {value}".format(value=self._value)

    def __repr__(self):
        if self._next:
            return "Node's value is {value} with next populated".format(value=self._value)
        else:
            return "Leaf Node's value is {value}".format(value=self._value)

    def __eq__(self, other):
        if self._value == other.getValue() and self._next == other.getNextNode():
            return True
        else:
            return False

    def __iter__(self):
        return _NodeIterator(self)

    def getValue(self):
        return self._value

    def getNextNode(self):
        return self._next

    def setNextNode(self, node):
        self._next = node


class _SinglyLinkedListIterator(object):

    def __init__(self, list):
        self.pointer = list

    def __iter__(self):
        return self

    def _handleIterationDepth(self, value, accumulator):
        for element in value:
            if isinstance(element, SinglyLinkedList):
                self._handleIterationDepth(element, accumulator)
            elif isinstance(element, _Node):
                if isinstance(element.getValue(), SinglyLinkedList) or isinstance(element.getValue(), _Node):
                    self._handleIterationDepth(element.getValue(), accumulator)
                else:
                    accumulator.append(element.getValue())
            else:
                accumulator.append(element)

    def __next__(self):
        if not self.pointer:
            raise StopIteration()

        currentValue = self.pointer.getValue()
        self.pointer = self.pointer.getNextNode()

        #TODO: this has a bug, its not working properly in suffixes from 2nd element
        if isinstance(currentValue, SinglyLinkedList) or isinstance(currentValue, _Node):
            accumulator = []
            self._handleIterationDepth(currentValue, accumulator)
            currentValue = accumulator

        return currentValue


class SinglyLinkedList(object):

    __slots__ = ['__head']

    def __init__(self, value=None):
        if value:
            object.__setattr__(self, '_SinglyLinkedList__head', _Node(value))
        else:
            object.__setattr__(self, '_SinglyLinkedList__head', None)

    def __iter__(self):
        return _SinglyLinkedListIterator(self.__head)

    def __setattr__(self, key, value):
        raise AttributeError('Attribute set to an existing list head not supported')


    def __eq__(self, other):
        if len(self) != len(other):
            return False
        pointer = self.__head
        for valueOther in other:
            if pointer.getValue() != valueOther:
                return False
            pointer = pointer.getNextNode()
        return True

    def __str__(self):
        args = '['
        if len(self) == 0:
            args += ''
        elif len(self) == 1:
            args += str(self.__head.getValue())
        else:
            for node in self.__head:
                if node.getNextNode():
                    args += str(node.getValue()) + ', '
                else:
                    args += str(node.getValue())
        args += ']'
        return args

    def __repr__(self):
        args = '['
        if len(self) == 0:
            args += ''
        elif len(self) == 1:
            args += str(self.__head.getValue())
        else:
            for node in self.__head:
                if node.getNextNode():
                    args += str(node.getValue()) + ', '
                else:
                    args += str(node.getValue())
        args += ']'
        return args

    def __len__(self):
        len = 0
        for node in self:
            len += 1
        return len

    def _copy(self):
        newlist = SinglyLinkedList()
        pointer = None
        for e in self:
            if not newlist.__head:
                object.__setattr__(newlist, '_SinglyLinkedList__head', _Node(e))
                pointer = newlist.__head
            else:
                pointer.setNextNode(_Node(e))
                pointer = pointer.getNextNode()
        return newlist, pointer

    def _appendNode(self, node):
        if self.__head:
            lastNode = None
            for h in self.__head:
                lastNode = h
            lastNode.setNextNode(node)
        else:
            object.__setattr__(self, '_SinglyLinkedList__head', node)

    def append(self, value):
        if self.__head:
            newlist, lastpointer = self._copy()
            lastpointer.setNextNode(_Node(value))
            return newlist
        else:
            object.__setattr__(self, '_SinglyLinkedList__head', _Node(value))
            return self

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

        newlist = SinglyLinkedList(self.__head.getValue())
        pointer = newlist.__head

        if self.__head.getNextNode():
            for h in self.__head.getNextNode():
                pointer.setNextNode(_Node(h.getValue()))
                pointer = pointer.getNextNode()

        pointer.setNextNode(anotherlist.__head)

        return newlist

    def update(self, oldValue, newValue):
        '''
        Figure 2.6 ys = update(xs, 2, 7)
        :param oldValue:
        :param newValue:
        :return: new list with an update
        '''

        newList = SinglyLinkedList()
        for node in self.__head:
            if node.getValue() == oldValue:
                newList._appendNode(_Node(newValue, node.getNextNode()))
                break
            newList.append(node.getValue())

        return newList

    def suffixes(self):
        '''
        Exercise 2.1 suffixes
        suffixes[1,2,3,4] = [[1,2,3,4], [2,3,4], [3,4], [4], [5], []]
        :return: a list of all suffixes of self in decreasing order of length
        '''

        newlist = SinglyLinkedList(self)
        if self.__head.getNextNode():
            for node in self.__head.getNextNode():
                newlist = newlist.append(SinglyLinkedList(node))
        newlist = newlist.append(SinglyLinkedList())
        return newlist


