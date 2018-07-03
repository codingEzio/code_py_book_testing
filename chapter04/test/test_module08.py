from nose.tools import timed
import time


# This decorator do such thing:
#   即用于 "测试 程序运行时长 是否超过 预期的时间"
#   the test case should be finish within the time you limited

#   if not,     test NOT PASS
#   if in it,   test PASS

@timed(.1)
def test_case01():
    time.sleep(.2)  # 测试用例并不需添此类代码 (e.g. sleep)

