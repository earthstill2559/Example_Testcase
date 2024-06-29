from coe_number.two_characters import twoCharacters
import unittest

class TwoCharatersTest(unittest.TestCase):
    def test_give_giveme(self):
        s = 'giveme'
        expected_output = 3
        result = twoCharacters(s)

        self.assertEqual(result, expected_output)

    def test_give_overwatch(self):
        s = 'overwatch'
        expected_output = 2
        result = twoCharacters(s)

        self.assertEqual(result, expected_output)

    def test_give_tyausguhsgdhhjgssdhg(self):
        s = 'tyausguhsgdhhjgssdhg'
        expected_output = 3
        result = twoCharacters(s)

        self.assertEqual(result, expected_output)

    def test_give_jajaja_1212(self):
        s = 'jajaja'*1212
        expected_output = 0
        result = twoCharacters(s)

        self.assertEqual(result, expected_output)

    def test_give_NoppadonCha(self):
        s = 'NoppadonCha'
        expected_output = 0
        result = twoCharacters(s)

        self.assertEqual(result, expected_output)

    def test_give_null(self):
        s = ' '
        expected_output = 0
        result = twoCharacters(s)

        self.assertEqual(result, expected_output)  

    def test_give_isdofpghewhsiydfuikjhqwhkjhsf(self):
        s = 'isdofpghewhsiydfuikjhqwhkjhsf'
        expected_output = 6
        result = twoCharacters(s)

        self.assertEqual(result, expected_output)                          

