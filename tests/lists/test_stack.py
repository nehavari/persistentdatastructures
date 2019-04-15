from unittest import TestCase
from lists.stack import Stack
import unittest

class TestStack(TestCase):

    def test_head(self):
        stack = Stack()
        stack.push('element 1')
        stack.push('element 2')
        output = stack.pop()
        self.assertEqual(output[0], 'element 2')
        self.assertEqual(stack.peek(), 'element 2')
        self.assertEqual(output[1].peek(), 'element 1')

    def test_tail(self):
        stack = Stack()
        stack.push('element 1')
        stack.push('element 2')
        self.assertEqual(stack.peek(), 'element 2')


if __name__ == '__main__':
    unittest.main()

