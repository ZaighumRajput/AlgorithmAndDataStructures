import unittest
import stack






def integer_to_string(integer, base):
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




class test_integer_to_string(unittest.TestCase):

    def test_binary(self):
        self.assertEqual(integer_to_string(3,2), '11')
        self.assertEqual(integer_to_string(2,2), '10')
        self.assertEqual(integer_to_string(1,2), '1')
        self.assertEqual(integer_to_string(5,2), '101')
        self.assertEqual(integer_to_string(10,2), '1010')

    def test_hexadecimal(self):
        self.assertEqual(integer_to_string(3,16), '3')
        self.assertEqual(integer_to_string(2,16), '2')
        self.assertEqual(integer_to_string(1,16), '1')
        self.assertEqual(integer_to_string(5,16), '5')
        self.assertEqual(integer_to_string(15,16), 'F')
        self.assertEqual(integer_to_string(16,16), '10')
        self.assertEqual(integer_to_string(18,16), '12')
        self.assertEqual(integer_to_string(128,16), '80')
        self.assertEqual(integer_to_string(10,16), 'A')
        self.assertEqual(integer_to_string(197,16), 'C5')
        self.assertEqual(integer_to_string(266,16), '10A')


    def test_octal(self):
        self.assertEqual(integer_to_string(3,8), '3')
        self.assertEqual(integer_to_string(2,8), '2')
        self.assertEqual(integer_to_string(1,8), '1')
        self.assertEqual(integer_to_string(5,8), '5')
        self.assertEqual(integer_to_string(10,8), '12')
        self.assertEqual(integer_to_string(16,8), '20')
        self.assertEqual(integer_to_string(18,8), '22')
        self.assertEqual(integer_to_string(128,8), '200')
        self.assertEqual(integer_to_string(144,8), '220')


if __name__ == '__main__':
	unittest.main()
