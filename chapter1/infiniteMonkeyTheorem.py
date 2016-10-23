import unittest
import random

def generate_string(lengthOfString):
    random_string = ''
    alphabet = 'abcdefghijklmnopqrstuvwxy '
    for _  in range(0,lengthOfString):
        random_string += random.choice(alphabet)
        #print(random_string)
    return random_string


def score_string(testString, goalString):
    '''Assigns a score based on how close testString is to goalString
    Return Type = (score, testString)
    '''
    if testString == goalString:
        return 100
    else:
        testStrCharList = list(testString)
        goalStrCharList = list(goalString)
        #should check length of both strings are equal
        correctCharactersBoolList = [ testChar == goalChar
                                     for (testChar, goalChar) in
                                     zip(testStrCharList, goalStrCharList)]
        score = (sum(correctCharactersBoolList)/len(correctCharactersBoolList))*100
        return(score)


class generate_string_test(unittest.TestCase):

    def test_generate_string_correctLength(self):
        self.assertEqual(len(generate_string(10)), 10)

class score_string_test(unittest.TestCase):

    def test_score_string_equal(self):
        score = score_string("Coffee is good", "Coffee is good")
        self.assertEqual(score, 100)

    def test_score_string_halfCorrect(self):
        score = score_string("abcdefghij","abcdexxxxx")
        self.assertEqual(score, 50)

if __name__ == '__main__':
    unittest.main()


