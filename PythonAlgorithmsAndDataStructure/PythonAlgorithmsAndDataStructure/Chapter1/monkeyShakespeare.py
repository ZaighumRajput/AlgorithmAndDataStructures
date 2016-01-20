import unittest
from random import choice

def Random_String_Generator(lengthOfString, listOfCharactersAllowed):
    """
    Generates a string of given length using characters from list provided


    """
    return "".join(choice(listOfCharactersAllowed) for _ in range(lengthOfString))

class Tests_Random_String_Generator(unittest.test):
    
    def SmokeTest(self):
        """
        Check if function exists and generates no errors
        """
        Random_String_Generator(5, ['a','b','c'])
