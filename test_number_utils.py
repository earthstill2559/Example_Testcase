from coe_number.number_utils import is_prime_list

import unittest

class primelisttest(unittest.TestCase):
    def test_give_1_2_3_is_prime(self):
        prime_list = [ 2, 3]
        for i in prime_list:
            is_prime = is_prime_list(i)
            self.assertTrue(is_prime)

    def test_give_2_is_prime(self):
        prime_list =  2 
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)    

    def test_give_5_7_11_is_prime(self):
        prime_list = [ 5,7,11 ]
        for i in prime_list:
            is_prime = is_prime_list(i)
            self.assertTrue(is_prime)  

    def test_give_0_is_prime(self):
        prime_list =  0 
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)   

    def test_give_negative_8_is_prime(self):
        prime_list =  -8
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)  


    def test_give_negative_91_is_prime(self):
        prime_list =  -91
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)                  
