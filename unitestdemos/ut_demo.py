import unittest


def add(x, y):
    return x+y


class Demo(unittest.TestCase):
    # 执行每个测试方法的时候都会执行一次setUp和tearDown
    def setUp(self):
        print("I am setUp")

    def test_demo1(self):
        print("my first unit test demo")
        self.assertEqual(add(10, 11), 21, "assert equal失败的时候才打印出这个消息内容")

    def test_demo2(self):
        print("my second unit test demo")
        self.assertEqual(add(1, 2), 5, "失败")

    def tearDown(self):
        print("I am tearDown")
