import unittest
import stack

def areBracketsBalanced(strToCheck):
    openingBrackets = {'('}
    BracketStack = stack.Stack()
    for character in strToCheck:
        if character in openingBrackets:
            BracketStack.push(character)
        else:
            if BracketStack.isEmpty():
                return False
            elif character == ')':
                BracketStack.pop()

    #strToCheck is balanced if each opening bracket has been
    #popped because of a closing bracket
    isBalanced = BracketStack.isEmpty()

    return isBalanced
class test_areBracketsBalanced(unittest.TestCase):

    def test_true(self):
        ListOfBalancedTestStrings = ['(1)',
                            '(1+(1+2))',
                            '(1+(1+(3 + x)))']

        for testString in ListOfBalancedTestStrings:
            self.assertTrue(areBracketsBalanced(testString))

    def test_false(self):
        ListOfUnBalancedTestStrings = ['( 1',
                                       '( 1 + (1 + 2)',
                                       '( 1 + ( + ( )']
        for testString in ListOfUnBalancedTestStrings:
            self.assertFalse(areBracketsBalanced(testString))

    '''
    These should be valid mathematical expressions
        def test_problematicExpression_True(self):
            ListOfProblematicTestStrings = ['',
                                            '1 + 1']
            for testString in ListOfProblematicTestStrings:
                self.assertTrue(areBracketsBalanced(testString))
    '''
    def test_problematicExpression_False(self):
        ListOfProblematicTestStrings = [')',
                                        '))1 + 1']
        for testString in ListOfProblematicTestStrings:
            self.assertFalse(areBracketsBalanced(testString))


if __name__ == '__main__':
    unittest.main()
