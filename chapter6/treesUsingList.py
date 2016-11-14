import unittest

class BinaryTree():

    def __init__(self, root_key):
        self.tree = [root_key, [], []]

    def insert_left(self):
        self.tree = self.tree
class Test_BinaryTree(unittest.TestCase):

    def test_constructor(self):
        sampleTree = BinaryTree("rootKey")
        self.assertEqual(sampleTree.tree,  ["rootKey", [], []])

    def test_insert_left(self):
        sampleTree = BinaryTree("rootKey")
        sampleTree.insertLeft("nodeLeft")
        self.assertEqual(sampleTree, ["rootKey", ["nodeLeft"], []])

if __name__ == '__main__':
    unittest.main()
