import unittest

from main import is_prime as f


class PrimeTest(unittest.TestCase):
    def test_prime_is_ok(self):
        for i in [2,3,5]:
            self.assertTrue(f(i))

    # def test_is_prime_raise_typeerror(self):
    #     with self.assertRaises(TypeError):
    #         f('strings')


if __name__ == '__main__':
    unittest.main()