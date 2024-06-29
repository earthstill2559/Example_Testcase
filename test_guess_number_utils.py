from coe_number.guess_number import guess_float, guess_int
import unittest
from unittest import mock

class GuessIntMockingTest(unittest.TestCase):
    @mock.patch('random.randint',return_value=1)
    def test(self,random_randint_mock):
        start = 5
        stop = 15
        expectedt_output = 1
        result = guess_int(start,stop)
        self.assertEqual(expectedt_output,result)
        random_randint_mock.assert_called()

    @mock.patch('random.randint',return_value=1)
    def test2(self,random_randint_mock):
        start = 10
        stop = 20
        expectedt_output = 1
        result = guess_int(start,stop)
        self.assertEqual(expectedt_output,result)
        random_randint_mock.assert_called()

    @mock.patch('random.randint',return_value=1)
    def test3(self,random_randint_mock):
        start = 2589
        stop = 20221
        expectedt_output = 1
        result = guess_int(start,stop)
        self.assertEqual(expectedt_output,result)
        random_randint_mock.assert_called() 

    @mock.patch('random.randint',return_value=50)
    def test4(self,random_randint_mock):
        start = 60
        stop = 100
        expectedt_output = 50
        result = guess_int(start,stop)
        self.assertEqual(expectedt_output,result)
        random_randint_mock.assert_called()

    @mock.patch('random.randint',return_value=568)
    def test5(self,random_randint_mock):
        start = 20
        stop = 80
        expectedt_output = 568
        result = guess_int(start,stop)
        self.assertEqual(expectedt_output,result)
        random_randint_mock.assert_called() 

class GuessFloatMockingTest(unittest.TestCase):
    @mock.patch('random.uniform',return_value=6.254)
    def test_float1(self,random_uniform_mock):
        start = 0
        stop = 10
        expectedt_result = 6.254
        result = guess_float(start,stop)
        self.assertEqual(expectedt_result,result)
        random_uniform_mock.assert_called()

    @mock.patch('random.uniform',return_value=8.256)
    def test_float2(self,random_uniform_mock):
        start = 10
        stop = 100
        expectedt_result = 8.256
        result = guess_float(start,stop)
        self.assertEqual(expectedt_result,result)
        random_uniform_mock.assert_called() 

    @mock.patch('random.uniform',return_value=78.369)
    def test_float3(self,random_uniform_mock):
        start = 79
        stop = 798
        expectedt_result = 78.369
        result = guess_float(start,stop)
        self.assertEqual(expectedt_result,result)
        random_uniform_mock.assert_called()

    @mock.patch('random.uniform',return_value=45.123)
    def test_float4(self,random_uniform_mock):
        start = 1234
        stop = 56789
        expectedt_result = 45.123
        result = guess_float(start,stop)
        self.assertEqual(expectedt_result,result)
        random_uniform_mock.assert_called()

    @mock.patch('random.uniform',return_value=611.254)
    def test_float5(self,random_uniform_mock):
        start = 1203
        stop = 56849
        expectedt_result = 611.254
        result = guess_float(start,stop)
        self.assertEqual(expectedt_result,result)
        random_uniform_mock.assert_called()                                      
