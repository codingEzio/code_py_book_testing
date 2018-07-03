import unittest


class Calculator:

    def add1(self, x, y):
        return x + y

    def add2(self, x, y):
        number_types = (int, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x + y
        else:
            raise ValueError


calc = 0

# 双剑合璧 XD
#   方法本身的错误处理 ( raise XXX )
#           +
#   unittest 的 assertRaises


class TestClass16(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global calc
        calc = Calculator()

    def setUp(self):
        print("\nIn setUp()...")

    def test_case01(self):
        self.assertEqual(calc.add1(2, 2), 4)

    def test_case02(self):
        self.assertEqual(calc.add2(2, 2), 4)

    def test_case03(self):
        # 预期 ValueError 得到的为 TypeError  (错误控制)
        self.assertRaises(ValueError, calc.add1, 2, 'two')

    def test_case04(self):
        # for this method "add2"
        #   add2 本身定义为: 若出错 raise ValueError
        #   此处抓到的 与预先定义的相同 即通过
        # 此方法能够确保 "即使程序出错, 其情况也仍在预期范围内"
        self.assertRaises(ValueError, calc.add2, 2, 'two')

    def tearDown(self):
        print("\nIn tearDown()...")

    @classmethod
    def tearDownClass(cls):
        global calc
        del calc
