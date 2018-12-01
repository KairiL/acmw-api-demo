from unittest import TestCase
from unittest.mock import patch
from acmw_api_demo.bad_math_utils import slow_math
import os


def mock_mult(a, b):
    # mock sum function without the long running time.sleep
    return int(a * b)

class TestSlowMath(TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.m=slow_math.SlowMather()

    def setUp(self):
        pass

    #Runs fast, but the result is meaningless.
    @patch('acmw_api_demo.bad_math_utils.slow_math.SlowMather.add', return_value=3)
    def test_slow_add_nonsense(self, mock_adder):
        self.assertEqual(mock_adder(2,3), 3)
        return

    #Actually takes the full 5 seconds to run
    def test_slow_add(self):
        self.assertEqual(self.m.add(2,3), 5)
        return

    #Runs so fast, it makes fast tests seem not fast.
    #Also verifies that our multiply is the inverse if divide.  Nifty.
    #@patch('acmw_api_demo.bad_math_utils.slow_math.SlowMather.multiply', side_effect=mock_mult)
    """
    def test_slow_divide(self):
        for i in range(8):
            for j in range(8):
                self.assertEqual(self.m.quick_divide(self.m.multiply(i,j+1), j+1), i)
        return
    """

    @patch('acmw_api_demo.bad_math_utils.slow_math.SlowMather.multiply', side_effect=mock_mult)
    def test_fastish_divide(self, mock_mult):
        for i in range(8):
            for j in range(8):
                #self.assertEqual(self.m.quick_divide(self.m.multiply(i,j+1), j+1), i)
                self.assertEqual(self.m.quick_divide(mock_mult(i,j+1), j+1), i)
        return
    
    #@patch('acmw_api_demo.bad_math_utils.slow_math.SlowMather.three_times_three', side_effect=mock_mult)
    def test_3x3_sad(self):
        self.assertEqual(self.m.three_times_three(), 9)