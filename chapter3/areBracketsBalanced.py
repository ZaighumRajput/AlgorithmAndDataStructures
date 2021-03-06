import unittest
import stack



OPENING_BRACKETS = '({['
CLOSING_BRACKETS = ')}]'

def doBracketsMatch(openBracket, closeBracket):
    '''what is a better data structure for this?
    '''
    return OPENING_BRACKETS.index(openBracket) == CLOSING_BRACKETS.index(closeBracket)

def areBracketsBalanced(strToCheck):

    BracketStack = stack.Stack()
    for character in strToCheck:
        if character in OPENING_BRACKETS:
            BracketStack.push(character)
        else:
            if BracketStack.isEmpty():
                return False
            elif character in CLOSING_BRACKETS and doBracketsMatch(BracketStack.peek(), character):
                BracketStack.pop()

    #strToCheck is balanced if each opening bracket has been
    #popped because of a closing bracket
    isBalanced = BracketStack.isEmpty()

    return isBalanced
class test_areBracketsBalanced(unittest.TestCase):

    def test_true(self):
        ListOfBalancedTestStrings = ['(1)',
                            '(1+(1+2))',
                            '(1+(1+(3 + x)))',
                                     '([1])',
                                     '[(1+1) in {a}]']

        for testString in ListOfBalancedTestStrings:
            self.assertTrue(areBracketsBalanced(testString))

    def test_false(self):
        ListOfUnBalancedTestStrings = ['( 1',
                                       '( 1 + (1 + 2)',
                                       '( 1 + ( + ( )',
                                       '[{',
                                       ']']
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

class test_doBracketsMatch_(unittest.TestCase):

    def test_match(self):
        self.assertTrue(doBracketsMatch('(', ')'))
        self.assertTrue(doBracketsMatch('{', '}'))
        self.assertTrue(doBracketsMatch('[', ']'))

    def test_notMatch(self):
        self.assertFalse(doBracketsMatch('(', ']'))

if __name__ == '__main__':
    unittest.main()
