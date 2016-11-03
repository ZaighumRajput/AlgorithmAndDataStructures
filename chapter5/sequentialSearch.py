import unittest


def sequential_search(aList, itemToFind):

    for item in aList:
        if item == itemToFind:
            return True

    return False

def ordered_sequential_search(aList, itemToFind):

    for item in aList:
        if item == itemToFind:
            return True
        elif item > itemToFind:
            return False

    return False

class test_sequential_test(unittest.TestCase):

    def test_can_find(self):
        testList = [4, 5, 1 , 2, 9, 10, 12, 0, 100]
        self.assertTrue(sequential_search(testList, 12))
        self.assertTrue(sequential_search(testList, 5))
        self.assertTrue(sequential_search(testList, 100))

    def test_cannot_find(self):
        testList = [4, 5, 1 , 2, 9, 10, 12, 0, 100]
        self.assertFalse(sequential_search(testList, 1000))
        self.assertFalse(sequential_search(testList, "Cat"))

class test_ordered_sequential_test(unittest.TestCase):

    def test_can_find(self):
        testList = [2,5, 6, 9, 10, 12, 16, 20, 100]
        self.assertTrue(ordered_sequential_search(testList, 12))
        self.assertTrue(ordered_sequential_search(testList, 5))
        self.assertTrue(ordered_sequential_search(testList, 100))

    def test_cannot_find(self):
        testList = [2,5, 6, 9, 10, 12, 16, 20, 100]
        self.assertFalse(ordered_sequential_search(testList, 1000))
        self.assertFalse(ordered_sequential_search(testList,15 ))


if __name__ == '__main__':
    unittest.main()

