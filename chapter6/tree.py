import unittest

class binary_tree():

    def __init__(self, root_key):
        self.key = root_key
        self.leftChild = None
        self.rightChild = None

    def insert_left(self, new_node):
        if (self.leftChild) is None:
            self.leftChild = binary_tree(new_node)
        else:
            subTree = binary_tree(new_node)
            subTree.leftChild = self.leftChild
            self.leftChild = subTree

    def getRootVal(self):
        return self.key

    def setRootVal(self, obj):
        self.key = obj

    def get_left_child(self):
        return (self.leftChild)

    def insert_right(self, new_node):
        if (self.rightChild) is None:
            self.rightChild = binary_tree(new_node)
        else:
            subTree = binary_tree(new_node)
            subTree.rightChild = self.rightChild
            self.rightChild = subTree

    def get_right_child(self):
        return self.rightChild


    def __str__(self):
        print(self.getRootVal())

class Test_BinaryTree(unittest.TestCase):

    def setUp(self):
        self.binaryTree = binary_tree("rootKey")

    def test_constructor(self):
        self.assertIsNotNone(self.binaryTree)

    def test_insert_left(self):
        self.binaryTree.insert_left("Left1")
        self.assertEqual(self.binaryTree.get_left_child().getRootVal(), "Left1")

    def test_insert_right(self):
        self.binaryTree.insert_right("Right1")
        self.assertEqual(self.binaryTree.get_right_child().getRootVal(),"Right1")

    def test_insert_right(self):
        self.binaryTree.insert_right("Right1")
        self.binaryTree.insert_right("Right2")
        self.assertEqual(self.binaryTree.get_right_child().getRootVal(),"Right1")


    def test_print(self):
        print(self.binaryTree)


if __name__ == '__main__':
    unittest.main()

