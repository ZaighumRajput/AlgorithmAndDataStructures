import unittest
import stack

def dec2AnyBase(integer, base):
    digits = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
    remainderStack = stack.Stack()
    currentInteger = integer
    remainder = 0
    binString = ''
    while currentInteger > 0:
        if base == 16:
            remainderStack.push(digits[currentInteger%base])
        else:
            remainderStack.push(currentInteger%base)

        currentInteger = currentInteger//base
    while(not remainderStack.isEmpty()):
        binString += str(remainderStack.pop())

    return binString


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


class test_dec2AnyBase(unittest.TestCase):

    def test_binary(self):
        self.assertEqual(dec2AnyBase(3,2), '11')
        self.assertEqual(dec2AnyBase(2,2), '10')
        self.assertEqual(dec2AnyBase(1,2), '1')
        self.assertEqual(dec2AnyBase(5,2), '101')
        self.assertEqual(dec2AnyBase(10,2), '1010')

    def test_hexadecimal(self):
        self.assertEqual(dec2AnyBase(3,16), '3')
        self.assertEqual(dec2AnyBase(2,16), '2')
        self.assertEqual(dec2AnyBase(1,16), '1')
        self.assertEqual(dec2AnyBase(5,16), '5')
        self.assertEqual(dec2AnyBase(15,16), 'F')
        self.assertEqual(dec2AnyBase(16,16), '10')
        self.assertEqual(dec2AnyBase(18,16), '12')
        self.assertEqual(dec2AnyBase(128,16), '80')
        self.assertEqual(dec2AnyBase(10,16), 'A')
        self.assertEqual(dec2AnyBase(197,16), 'C5')
        self.assertEqual(dec2AnyBase(266,16), '10A')


    def test_octal(self):
        self.assertEqual(dec2AnyBase(3,8), '3')
        self.assertEqual(dec2AnyBase(2,8), '2')
        self.assertEqual(dec2AnyBase(1,8), '1')
        self.assertEqual(dec2AnyBase(5,8), '5')
        self.assertEqual(dec2AnyBase(10,8), '12')
        self.assertEqual(dec2AnyBase(16,8), '20')
        self.assertEqual(dec2AnyBase(18,8), '22')
        self.assertEqual(dec2AnyBase(128,8), '200')
        self.assertEqual(dec2AnyBase(144,8), '220')
if __name__ == '__main__':
    unittest.main()
