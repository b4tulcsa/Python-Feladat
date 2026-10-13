import unittest

def calculator(a: float, b: float, c: str):
    if c == "+":
        return a + b
    elif c == "-":
        return a - b
    elif c == "*":
        return a * b
    elif c == "/":
        return a / b

class TestCalcFunction(unittest.TestCase):

    def test_osszeadas(self):
        self.assertGreater(calculator(5, 12, "+"), 0)

    def test_kivonas(self):
        self.assertLess(calculator(10, 2, "-"), 10)

    def test_szorzas(self):
        self.assertGreater(calculator(4, 4, "*"), 4)

    def test_osztas(self):
        self.assertLess(calculator(9, 3, "/"), 9)

    def test_negativ(self):
        self.assertGreater(calculator(9, -13, "-"), 9)


if __name__ == '__main__':
    unittest.main()

#print(calculator(int(input("1. szám: ")), int(input("2. szám: ")), input("művelet: ")))