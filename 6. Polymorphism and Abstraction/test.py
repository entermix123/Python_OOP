# test circle
import unittest


class ShapesTests(unittest.TestCase):
    def test(self):
        c = Circle(5)
        self.assertEqual(c.calculate_area(), 78.53981633974483)
        self.assertEqual(c.calculate_perimeter(), 31.41592653589793)


if __name__ == "__main__":
    unittest.main()