import unittest

from calc import add, subtract, multiply, divide


class TestCalc(unittest.TestCase):

    def test_add(self):
        result = add(5, 10)
        self.assertEqual(result, 15)

    def test_subtract(self):
        self.assertEqual(subtract(20,10), 10)

    def test_multipy(self):
        self.assertEqual(multiply(20,10), 200)

    def test_divide(self):
        self.assertEqual(divide(20, 10), 2)


if __name__ == '__main__':
    unittest.main()