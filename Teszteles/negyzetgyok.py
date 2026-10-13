import unittest
import math

def negyzetgyok(szam: int):
    return math.sqrt(szam)

a = int(input("Adj egy számot: "))
if a >= 0:
    print(negyzetgyok(a))
else:
    print("Nem lehet negativ")

class TestNegyzetGyokFunction(unittest.TestCase):

    def test_negyzetgyok(self):
        ertek = negyzetgyok(5)
        self.assertGreater(ertek, 0)

    def test_negative(self):
        ertek = negyzetgyok(-1)
        self.assertLess(ertek, 0)

    def test_nagyszam(self):
        ertek = negyzetgyok(3030515151)
        self.assertGreater(ertek, 0)

if __name__ == '__main__':
    unittest.main()
