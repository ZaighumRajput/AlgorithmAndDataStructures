import unittest
import stack


def revString(stringToReverse):
    ''' Uses a Stack to reverse a string
    '''
    stringStack = stack.Stack()
    for letter in stringToReverse:
        stringStack.push(letter)

    reversedString = ''
    while not stringStack.isEmpty():
        reversedString += stringStack.pop()

    return reversedString

class test_revString(unittest.TestCase):

    def test_revString(self):
        testString = "abc"
        self.assertEqual(revString(testString), "cba")
        testString2 = "wrote"
        self.assertEqual(revString(testString2), "etorw")

if __name__ == '__main__':
    unittest.main()
