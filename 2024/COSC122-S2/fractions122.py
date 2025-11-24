"""
COSC122 QUIZ 1
SEAN FAULKNER
"""

class Fraction():
    '''Defines a Fraction type that has an integer numerator and a non-zero integer denominator'''

    def __init__(self, num=0, denom=1):
        ''' Creates a new Fraction with numerator num and denominator denom'''
        if isinstance(num, int) and isinstance(denom, int):
            self.numerator = num
            if denom != 0:
                self.denominator = denom
            else:
                raise ZeroDivisionError
        else:
            raise ValueError('Numerator and denominator must be ints')
    def __str__(self):
        """returns the fraction"""
        return f"{self.numerator}/{self.denominator}"
    def __repr__(self):
        """shows us the initalliser"""
        return f"Fraction({self.numerator}, {self.denominator})"
    def __add__(self, other):
        '''Return a new unreduced fraction obtained by adding other to self'''
        num = (self.numerator*other.denominator) + (other.numerator*self.denominator)
        denom = self.denominator * other.denominator
        return Fraction(num, denom)
    def __mul__(self, other):
        '''Implement the multiply operator'''
        num = self.numerator * other.numerator
        denom = self.denominator * other.denominator
        return Fraction(num, denom)
    def __eq__(self, other):
        """Implement the '==' operator on Fractions"""
        result = False
        sum_1 = self.numerator * other.denominator
        sum_2 = other.numerator * self.denominator
        if sum_1 == sum_2:
            result = True
        return result

def find_gcd(num1, num2):
    """ 
    Returns the Greatest Common Divisor (GCD) of num1 and num2. 
    Assumes num1 and num2 are positive integers. 
    """
    smaller = min(num1, num2)
    for i in range(smaller, 1, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i
    return 1

class ReducedFraction(Fraction):
    """A version of Fraction that always keeps itself in maximally reduced form"""
    
    def __init__(self, numerator=0, denominator=1):
        """ Initialiser, given both numerator and denominator """
        super().__init__(numerator, denominator)  # use Fraction.__init__ 
        self._reduce()
    def _reduce(self):
        """ Reduces the fraction to its simplest possible form.
        NOTE: This method does NOT return anything, 
              it updates self.numerator and self.denominator
        """
        divisor = find_gcd(self.numerator, self.denominator)
        self.numerator = int(self.numerator/divisor)
        self.denominator = int(self.denominator/divisor)
    def __repr__(self):
        """Shows us the initialiser class"""
        return f"ReducedFraction({self.numerator}, {self.denominator})"
    def __add__(self, other):
        """adds two fractions"""
        fraction_result = super().__add__(other)   # uses the __add__ method from Fraction
        reduced_result = ReducedFraction(fraction_result.numerator,fraction_result.denominator)
        return reduced_result
    def __mul__(self, other):
        """Multiplys a fraction and then simplfies it"""
        # You're nearly there
        fraction_result = super().__mul__(other)
        reduced_result = ReducedFraction(fraction_result.numerator,fraction_result.denominator)
        return reduced_result

class MixedNumber():
    """makes a mixed fraction using a whole number and fraction"""
    def __init__(self, whole_part=0, fraction_part=1):
        """Initialiser, given mixed num and fraction"""
        extra_fraction = fraction_part.numerator//fraction_part.denominator
        self.whole_part = whole_part + extra_fraction
        fraction_part.numerator -= (extra_fraction*fraction_part.denominator)
        self.fraction_part = ReducedFraction(fraction_part.numerator,fraction_part.denominator)
    def __repr__(self):
        """Shows us the initialiser of the class"""
        return f"MixedNumber({self.whole_part}, {repr(self.fraction_part)})"
    def __str__(self):
        """supplys the format of the result of the class"""
        x = f"{self.whole_part} and {self.fraction_part.numerator}/{self.fraction_part.denominator}"
        return x
    def __add__(self, other):
        """adds two mixed number together"""
        fraction = ReducedFraction(self.fraction_part.numerator,self.fraction_part.denominator)
        fraction += ReducedFraction(other.fraction_part.numerator,other.fraction_part.denominator)
        whole_part = self.whole_part + other.whole_part
        return MixedNumber(whole_part, fraction)