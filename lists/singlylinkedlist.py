class SinglyLinkedList:
    class _Node:
        def __init__(self, value, next):
            self._value = value
            self._next = next

        def __next__(self, node):
            self._next = node

    def __init__(self, value):
        self._head = self._Node(value, None)

    def append(self, element):
        node = self._head
        while not node.next():
            node.next(self._Node(element, None))

    def getNextNode(self):
        return self.__next

    def __iter__(self):
        return self

    def __next__(self):
        return self.__next

def append(list1, list2):
    for node in list1:
        print(node)
    for node in list2:
        print(node)

#
# if __name__ == '__main__':
#     list1 = Node(1).setNextNode(Node(2)).setNextNode(Node(3)).setNextNode(Node(4))
#     print(list1)
#     list2 = Node(5).setNextNode(Node(6)).setNextNode(Node(7)).setNextNode(Node(8))
#     print(list2)
#     # append(list1, list2)