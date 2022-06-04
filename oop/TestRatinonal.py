import unittest
from oop import Rational

class RationalTest(unittest.TestCase):
    def test_different_payda_add(self):
        r1 = Rational(1, 2)
        r2 = Rational(3, 6)

        r3 = r1 + r2

        self.assertEqual(6, r3.getPay())
        self.assertEqual(6, r3.getPayda())







if __name__ == '__main__':
    unittest.main()
