import unittest
import Complex
import Methods


class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, False)  # add assertion here

    def test_sum(self):
        self.assertEqual(Methods.sum(16, 11), 17)

    def test_Complex_instance(self):
        self.assertIsInstance(Complex.Complex(3, 5), type(Complex))








if __name__ == '__main__':
    unittest.main()
