import unittest

def gyakjegy(szam: int):
    if szam <= 0 or szam > 100:
        return "Ervenytelen szam"
    elif szam >= 90:
        return 5
    elif szam >= 80:
        return 4
    elif szam >= 70:
        return 3
    elif szam >= 60:
        return 2
    elif szam < 60:
        return 1

class TestGyakFunction(unittest.TestCase):

    def test_rosszszam(self):
        self.assertEqual(gyakjegy(-5), "Ervenytelen szam")

    def test_masikrossz(self):
        self.assertEqual(gyakjegy(101), "Ervenytelen szam")
        
    def test_joszam5(self):
        self.assertEqual(gyakjegy(90), 5)
        
    def test_joszam4(self):
        self.assertEqual(gyakjegy(80), 4)

    def test_joszam3(self):
        self.assertEqual(gyakjegy(70), 3)

    def test_joszam2(self):
        self.assertEqual(gyakjegy(60), 2)

    def test_joszam1(self):
        self.assertEqual(gyakjegy(50), 1)
            
        


if __name__ == '__main__':
    unittest.main()