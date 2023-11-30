import unittest
import time


class MyTest(unittest.TestCase):

    def test_something(self):
        start_time = time.time()
        time.sleep(1)                   # tested function
        end_time = time.time()
        diff = end_time - start_time
        print(f"Test took time {diff} seconds to complete")
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
