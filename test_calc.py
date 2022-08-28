import unittest

from calc import add, subtract, multiply, divide


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 10), 15)
        self.assertEqual(add(-5, 10), 5)
        self.assertEqual(add(-5, -10), -15)

    def test_subtract(self):
        self.assertEqual(subtract(20, 10), 10)
        self.assertEqual(subtract(-5, 10), -15)
        self.assertEqual(subtract(-5, -10), 5)

    def test_multipy(self):
        self.assertEqual(multiply(20,10), 200)
        self.assertEqual(multiply(-5, 10), -50)
        self.assertEqual(multiply(-5, -10), 50)

    def test_divide(self):
        self.assertEqual(divide(20, 10), 2)


if __name__ == '__main__':
    unittest.main()