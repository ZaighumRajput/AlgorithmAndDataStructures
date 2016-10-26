import unittest

def reverse_string(stringToReverse):
    '''
    Reverse string using recurssion
    '''
    #base case
    #must call itself
    if(len(stringToReverse) <= 1):
        return stringToReverse
    else:
        return stringToReverse[-1] + reverse_string(stringToReverse[0:-1])

def isPalindrome(stringToTest):
    return reverse_string(stringToTest) == stringToTest


class testReverseString(unittest.TestCase):

    def test_work(self):
        self.assertEqual("a", reverse_string("a"))
        self.assertEqual("cba", reverse_string("abc"))
        self.assertEqual("kayak", reverse_string("kayak"))

class testIsPalindrome(unittest.TestCase):

    def test_true(self):
        self.assertTrue(isPalindrome("kayak"));

if __name__ == "__main__":
    unittest.main()
