import unittest

def generate_string():
    pass

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

    def test_generate_string_smoke(self):
        generate_string()

class score_string_test(unittest.TestCase):

    def test_score_string_equal(self):
        score = score_string("Coffee is good", "Coffee is good")
        self.assertEqual(score, 100)

    def test_score_string_halfCorrect(self):
        score = score_string("abcdefghij","abcdexxxxx")
        self.assertEqual(score, 50)

if __name__ == '__main__':
    unittest.main()


