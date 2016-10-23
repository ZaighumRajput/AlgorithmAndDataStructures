import unittest
def squareroot(n):
    ''' Newton's method for finding squareroot
    '''
    oldGuess = n/2
    newGuess = 0
    for guessNumber in range(0,20):
        newGuess = 1/2 * (oldGuess + n/oldGuess)
        oldGuess = newGuess
        print(newGuess)
    return newGuess

def distanceIsLessThanEpsilon(a,b, epsilon):
    '''From Real Analysis
        To see if the distance between two numbers a, b is close to some
        small arbitrary number epsilon.
        When we cannot check if a and b are equal (e.g in the case of
        irrationals)
        we can still check if a, b are close up to an error of e
    '''
    return abs(a-b) < epsilon

class squareroot_test(unittest.TestCase):

    def test_properSquare(self):
        self.assertEqual(squareroot(25), 5);

    def test_irrational(self):
        self.assertTrue(distanceIsLessThanEpsilon(squareroot(2), 1.414213,
                                                   epsilon=0.0001))

    def test_properSqualWithEpsilonDefinition(self):
        self.assertTrue(distanceIsLessThanEpsilon(squareroot(25), 5,
                                                   epsilon=0.0000001))



class epsilon_test(unittest.TestCase):

    def test_truth(self):
        self.assertTrue(distanceIsLessThanEpsilon(1,0.9999, epsilon=0.0001))

    def test_false(self):
        self.assertFalse(distanceIsLessThanEpsilon(1, 1.1, epsilon = 0.0001))
if __name__ == '__main__':
    unittest.main()

