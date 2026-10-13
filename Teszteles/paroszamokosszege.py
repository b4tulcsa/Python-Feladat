import unittest

def parosszamok(a: int, b: int):
    parososz = 0
    for i in range(a, b+1):
        if i % 2 == 0:
            parososz += i
    return parososz        


class TestParosokFunction(unittest.TestCase):

    def test_joszam(self):
        self.assertEqual(parosszamok(42, 100), 2130)

    def test_joszam1(self):
        self.assertGreater(parosszamok(0, 10), 0)

    def test_joszam2(self):
        self.assertLess(parosszamok(-40, -10), 0)

if __name__ == '__main__':
    unittest.main()