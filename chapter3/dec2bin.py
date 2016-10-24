import unittest
import stack

def dec2bin(integer):
    remainderStack = stack.Stack()
    currentInteger = integer
    remainder = 0
    binString = ''
    while currentInteger > 0:
        remainderStack.push(currentInteger%2)
        currentInteger = currentInteger//2
    while(not remainderStack.isEmpty()):
        binString += str(remainderStack.pop())

    return binString
class test_dec2bin(unittest.TestCase):

    def test_correct(self):
        self.assertEqual(dec2bin(3), '11')
        self.assertEqual(dec2bin(2), '10')
        self.assertEqual(dec2bin(1), '1')
        self.assertEqual(dec2bin(5), '101')
        self.assertEqual(dec2bin(10), '1010')

if __name__ == '__main__':
    unittest.main()
