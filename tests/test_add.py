import unittest
from asperin.utils.add import add


class TestAdd(unittest.TestCase):
    def test_add_int(self):
        result = add(5, 5)
        self.assertEqual(result, 10)


if __name__ == "__main__":
    unittest.main()
