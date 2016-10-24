import unittest

class Queue():

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class test_queue(unittest.TestCase):

    def setUp(self):
        self.testQueue = Queue()

    def test_initialization(self):
        self.assertIsNotNone(self.testQueue)

    def test_isEmpty(self):
        self.assertTrue(self.testQueue)

    def test_enqueue(self):
        self.testQueue.enqueue("FirstItem")
        self.assertFalse(self.testQueue.isEmpty())

    def test_dequeue(self):
        self.testQueue.enqueue("FirstItem")
        self.testQueue.enqueue("SecondItem")
        self.assertEqual(self.testQueue.dequeue(), "FirstItem")
        self.assertEqual(self.testQueue.dequeue(), "SecondItem")

    def test_size(self):
        self.testQueue.enqueue("FirstItem")
        self.testQueue.enqueue("SecondItem")
        self.assertEqual(self.testQueue.size(), 2)
        self.testQueue.dequeue()
        self.assertEqual(self.testQueue.size(), 1)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
