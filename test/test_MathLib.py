import unittest

from src.MathLib import MathLib
from src.MathRequest import MathRequest


class TestMathLib(unittest.TestCase):

    def setUp(self):
        pass

    def test_execute_add_get_result(self):
        #given
        mathRequest = MathRequest(3, 'add', 4)

        #when
        MathLib.execute(mathRequest)

        #then
        self.assertEqual(mathRequest.get_res(), 7)

    def test_execute_sub_get_result(self):
        # given
        mathRequest = MathRequest(3, 'sub', 4)

        # when
        MathLib.execute(mathRequest)

        # then
        self.assertEqual(mathRequest.get_res(), -1)

    def test_execute_mul_get_result(self):
        # given
        mathRequest = MathRequest(3, 'mul', 4)

        # when
        MathLib.execute(mathRequest)

        # then
        self.assertEqual(mathRequest.get_res(), 12)

    def test_execute_div_get_result(self):
        # given
        mathRequest = MathRequest(3, 'div', 4)

        # when
        MathLib.execute(mathRequest)

        # then
        self.assertEqual(mathRequest.get_res(), 0.75)

    def test_execute_pow_get_result(self):
        # given
        mathRequest = MathRequest(3, 'pow', 4)

        # when
        MathLib.execute(mathRequest)

        # then
        self.assertEqual(mathRequest.get_res(), 81)

    def test_execute_root_get_result(self):
        # given
        mathRequest = MathRequest(3, 'root', 4)

        # when
        MathLib.execute(mathRequest)

        # then
        self.assertEqual(mathRequest.get_res(), 1.32)

if __name__ == '__main__':
    unittest.main()