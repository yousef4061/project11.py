
class Fraction:
    def __init__(self, numerator, denominator):
        # properties
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    # methods
    def simplify(self):
        def gcd(a, b):
            while b:
                a, b = b, a % b
                return a
        div = gcd(self.numerator, self.denominator)
        self.numerator //= div
        self.denominator //= div

    def show(self):
        return f"{self.numerator}/{self.denominator}"
    
    def add(self, other):
        new_num = self.numerator * other.denominator + other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)
    
if __name__ == "__main__":
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        f3 = f1.add(f2)
        print(f3.show())
