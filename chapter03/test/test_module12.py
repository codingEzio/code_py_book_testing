import unittest
import sys

# 有"条件"地跳过部分测试
#   by using the decorators of unittest

# skip method list
#   skip(reason)                say something why u skip that
#   skipIf(cond,reason)         when .. true skip, say something
#   skipUnless(cond,reason)     n
#   expectedFailure()


class TestClass13(unittest.TestCase):

    @unittest.skip("demonstrating unconditional skipping")
    def test_case01(self):
        self.fail("FATAL")

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_case02(self):
        # Windows specific testing code
        pass

    @unittest.skipUnless(sys.platform.startswith("linux"), "requires Linux")
    def test_case03(self):
        # Linux specific testing code
        pass
