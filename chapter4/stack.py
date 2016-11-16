import unittest

class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def isEmpty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Stack_test(unittest.TestCase):

    def setUp(self):
        self.testStack = Stack()

    def test_initialize(self):
        self.assertIsNotNone(self.testStack)

    def test_isEmpty(self):
        self.assertTrue(self.testStack.isEmpty())

    def test_push(self):
        self.testStack.push("FirstItem")
        self.assertFalse(self.testStack.isEmpty())

    def test_peek(self):
        self.testStack.push("FirstItem")
        self.assertEqual(self.testStack.peek(), "FirstItem")

    def test_pop(self):
        self.testStack.push("FirstItem")
        self.assertEqual(self.testStack.pop(), "FirstItem")
        self.assertTrue(self.testStack.isEmpty())

    def test_size(self):
        self.assertEqual(self.testStack.size(), 0)
        self.testStack.push("FirstItem")
        self.assertEqual(self.testStack.size(), 1)
        self.testStack.push("SecondItem")
        self.assertEqual(self.testStack.size(), 2)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
