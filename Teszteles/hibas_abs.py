import unittest

def hibasabs(szam: int):
    return abs(szam)

class TestAbsFunction(unittest.TestCase):

    def test_one_negative(self):
        ertek = hibasabs(-5)
        self.assertEqual(ertek, 5)


    def test_one_pos(self):
        ertek = hibasabs(5)
        self.assertGreater(ertek, 0)

unittest.main()