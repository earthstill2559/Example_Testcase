from coe_number.alternating_characters import alternating
import unittest

class Alternating(unittest.TestCase):
    def test_give_AAAAABBBB(self):
        text = 'AAAAABBBB'
        expected_output = 7

        result = alternating(text)

        self.assertEqual(result, expected_output, f'Should be {expected_output}')

    def test_give_BBBBBBBBBBBBBBAAAAAA(self):
        text = 'BBBBBBBBBBBBBBAAAAAA'
        expected_output = 18

        result = alternating(text)

        self.assertEqual(result, expected_output, f'Should be {expected_output}')  

    def test_give_BBAABABAABAA(self):
        text = 'BBAABABAABAA'
        expected_output = 4

        result = alternating(text)

        self.assertEqual(result, expected_output, f'Should be {expected_output}')

    def test_give_BBAABABAABABABABAAA(self):
        text = 'BBAABABAABAABABABABAAA'
        expected_output = 6

        result = alternating(text)

        self.assertEqual(result, expected_output, f'Should be {expected_output}')   

    def test_give_BBAABABAABAAAAAAAAAB(self):
        text = 'BBAABABAABAAAAAAAAAAAB'
        expected_output = 13

        result = alternating(text)

        self.assertEqual(result, expected_output, f'Should be {expected_output}')  

    def test_give_BABBBAAABABABBBB(self):
        text = 'BABBBAAABABABBBB'
        expected_output = 7

        result = alternating(text)

        self.assertEqual(result, expected_output, f'Should be {expected_output}')   
        
    def test_give_BBBBBAAAAABBAA(self):
        text = 'BBBBBAAAAABBAA'
        expected_output = 10

        result = alternating(text)

        self.assertEqual(result, expected_output, f'Should be {expected_output}')         

