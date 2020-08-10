import unittest


class Simple_test(unittest.TestCase):
    # # 执行每个类的时候都会执行一次setUp和tearDown
    @classmethod
    def setUpClass(cls):
        print("Init class\n")
        Simple_test.foo = list(range(10))

    def test_first(self):
        print(str(Simple_test.foo))
        self.assertEqual(Simple_test.foo.pop(), 9)

    def test_second(self):
        print(str(Simple_test.foo))
        self.assertEqual(Simple_test.foo.pop(), 8)

    @classmethod
    def tearDownClass(cls):
        print("end class")

    if __name__ == '__main__':
        unittest.main()
