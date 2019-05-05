'''
This is not a persistent stack. This is meant for using internally for other
data structure.
'''

class Node:
    def __init__(self, value, nextt=None):
        self.__value = value
        self.__next = nextt

    def setValue(self, value):
        self.__value = value

    def getValue(self):
        return self.__value

    def setNextNode(self, nextt):
        self.__next = nextt

    def getNextNode(self):
        return self.__next


class Stack:
    def __init__(self, node=None):
        self.__head = node

    def isEmpty(self):
        return True if self.__head is None else False

    def push(self, e):
        if not self.__head:
            self.__head = Node(e)
        else:
            node = Node(e)
            node.setNextNode(self.__head)
            self.__head = node

    def pop(self):
        if not self.__head:
            raise Exception('Stack is empty')
        value = self.__head.getValue()
        self.__head = self.__head.getNextNode()
        return value

    def peek(self):
        if not self.__head:
            raise Exception('Stack is empty')
        return self.__head.getValue()
