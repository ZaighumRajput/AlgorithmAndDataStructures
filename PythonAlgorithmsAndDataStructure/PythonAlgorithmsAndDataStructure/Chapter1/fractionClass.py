def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n


class Fraction:

    def __init__(self, top, bottom):

        self._num = top
        self._den = bottom

    def __str__(self):
        
        return str(self._num) + "/" + str(self._den)


    def __add__(self, otherFraction):

        newnum = self._num*otherFraction._den + self._den*otherFraction._num
        newden = self._den * otherFraction._den
        common = gcd(newnum, newden)
        
        return Fraction(newnum//common, newden//common)

    def __sub__(self, otherFraction):

        newnum = self._num*otherFraction._den - self._den*otherFraction._num
        newden = self._den * otherFraction._den
        common = gcd(newnum, newden)
        
        return Fraction(newnum//common, newden//common)

    def __mul__(self, other):
        newnum  = self._num * other._num
        newden = other._den * other._den

        common = gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)

    def __truediv__(self, other):
        newnum = self._num * other._den
        newden = self._den *  other._num

        common = gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)
         
    def getNum(self):
        return self._num

    def getDen(self):
        return self._den

    def __eq__(self, other):
        firstnum = self._num * other._den
        secondnum = other._num * self._den

        return firstnum == secondnum

    def __lt__(self, other):
        firstnum = self._num * other._den
        secondnum = other._num * self._den

        return firstnum < secondnum

    def __gt__(self, other):
        firstnum = self._num * other._den
        secondnum = other._num * self._den

        return firstnum > secondnum        
