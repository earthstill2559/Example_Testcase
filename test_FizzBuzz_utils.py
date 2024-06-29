from coe_number.fizzbuzz_utils import fizzbuzz
import unittest
class primelisttest(unittest.TestCase):
    def test_give_3_is_fizz(self):
        num = 3
        result = fizzbuzz(num)
        self.assertEqual(result,'Fizz')

    def test_give_24_is_fizz(self):
        num = 24
        result = fizzbuzz(num)
        self.assertEqual(result,'Fizz')

    def test_give_96_is_fizz(self):
        num = 96
        result = fizzbuzz(num)
        self.assertEqual(result,'Fizz')  

    def test_give_5_is_buzz(self):
        num = 5
        result = fizzbuzz(num)
        self.assertEqual(result,'Buzz')  

    def test_give_50_is_buzz(self):
        num = 50
        result = fizzbuzz(num)
        self.assertEqual(result,'Buzz')  

    def test_give_15_is_fizzbuzz(self):
        num = 15
        result = fizzbuzz(num)
        self.assertEqual(result,'FizzBuzz')   

    def test_give_195_is_fizzbuzz(self):
        num = 195
        result = fizzbuzz(num)
        self.assertEqual(result,'FizzBuzz')               

                 