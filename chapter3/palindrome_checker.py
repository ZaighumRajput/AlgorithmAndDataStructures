import unittest
from collections import deque

def isPalindrome( string_to_test):
    palindromeDeque = deque()
    for letter in string_to_test:
        palindromeDeque.append(letter)

    print(palindromeDeque)
    isEqual = True
    while len(palindromeDeque) > 1 and isEqual:
        if palindromeDeque.pop() !=  palindromeDeque.popleft():
            isEqual = False

    return isEqual




class test_palindrome_check(unittest.TestCase):

    def test_true(self):
        self.assertTrue(isPalindrome("AA"))
        self.assertTrue(isPalindrome("radar"))

    def test_false(self):
        self.assertFalse(isPalindrome("not"))
        self.assertFalse(isPalindrome("palindrome"))


if __name__ == "__main__":
    unittest.main()
