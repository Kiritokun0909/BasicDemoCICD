import unittest
from script2 import multiply

class TestScript2(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(0, 5), 0)

if __name__ == '__main__':
    unittest.main()
