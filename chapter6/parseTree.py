import unittest
from tree import binary_tree
from stack import Stack

openBracket = [ '(' ]
operator = [ '+', '-', '/', '*']
closeBracket = [')']
operand = ['0', '1', '2', '3', '4', '5', '6', '7','8', '9']


class parse_tree():
    def __init__(self, expression):

        stack = Stack()
        self.tree = binary_tree('')
        stack.push(self.tree)
        currentTree = self.tree

        for token in expression:
            if token in openBracket:
                currentTree.insert_left('')
                stack.push(currentTree)
                currentTree = currentTree.get_left_child()
            elif token in operator:
                currentTree.setRootVal(token)
                currentTree.insert_right('')
                stack.push(currentTree)
                currentTree = currentTree.get_right_child()
            elif token in operand:
                currentTree.setRootVal(int(token))
                parent = stack.pop()
                currentTree = parent
            elif token in closeBracket:
                parent = stack.pop()
                currentTree = parent
            else:
                #throw exception
                pass

    def evaluate(self):
        pass


class test_parse_tree(unittest.TestCase):

    def test_constructor(self):
        self.parseTree = parse_tree("(3+(4*5))")
        self.assertIsNotNone(self.parseTree)

    def test_simple(self):
        openTree = parse_tree("(3+5)")
        self.assertEqual(openTree.tree.getRootVal(), "+")
        self.assertEqual(openTree.tree.get_left_child().getRootVal(), 3)
        self.assertEqual(openTree.tree.get_right_child().getRootVal(), 5)

if __name__ == '__main__':
    unittest.main()

    '''
    expr = "(3+(4*5))"
    for char in expr:
        print(char)
    '''

    test = parse_tree("(3+(4*5))")

