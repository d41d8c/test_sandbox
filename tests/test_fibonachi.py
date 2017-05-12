import unittest
import fibon


class TestFibonachi(unittest.TestCase):
    def test_fibonachi(self):
        self.assertEqual(fibon.fibonachi(8), 21)
        self.assertEqual(fibon.fibonachi(2), 1)
        self.assertEqual(fibon.fibonachi(0), 0)
        # self.assertEqual(fibon.fibonachi(-4), -3)

    def test_fibonachi2(self):
        self.assertNotEqual(fibon.fibonachi(8), 23)
        self.assertNotEqual(fibon.fibonachi(2), 99)
        #     self.assertEqual(0, 0)
        #     self.assertTrue(-100, -354224848179261915075)
        #     self.assertTrue(100, 354224848179261915075)
        #
        # def test_fibonachi1(self):
        #     self.assertTrue(-101, 573147844013817084101)
        #     self.assertTrue(-1, 1)
        #
        # def test_fibonachi2(self):
        #     self.assertTrue(3, 2)
        #     self.assertTrue(4, 3)
        #     self.assertTrue(5, 5)


if __name__ == '__main__': # pragma no cover
    import os, unittest
    tests = unittest.TestLoader().discover('.')
