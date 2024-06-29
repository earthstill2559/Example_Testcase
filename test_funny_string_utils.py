from coe_number.funny_string import funny_string
import unittest

class FunnyStringTest(unittest.TestCase):
    def test_give_iuyt(self):
        text = 'iuyt'
        expected_output = 'Not Funny'

        result = funny_string(text)

        self.assertEqual(result, expected_output, f'Should be {expected_output}')

    def test_give_uiot(self):
        text = 'uiot'
        expected_output = 'Not Funny'

        result = funny_string(text)

        self.assertEqual(result, expected_output, f'Should be {expected_output}')
        
    def test_give_ilove(self):
        text = 'ilove'
        expected_output = 'Not Funny'

        result = funny_string(text)

        self.assertEqual(result, expected_output, f'Should be {expected_output}') 

    def test_give_bdwy(self):
        text = 'bdwy'
        expected_output = 'Funny'

        result = funny_string(text)

        self.assertEqual(result, expected_output, f'Should be {expected_output}') 

    def test_give_malayalam(self):
        text = 'malayalam'
        expected_output = 'Funny'

        result = funny_string(text)

        self.assertEqual(result, expected_output, f'Should be {expected_output}')   

    def test_give_j(self):
        text = 'j'
        expected_output = 'not at all'

        result = funny_string(text)

        self.assertEqual(result, expected_output, f'Should be {expected_output}') 

    def test_give_no_string(self):
        text = ''
        expected_output = 'not at all'

        result = funny_string(text)

        self.assertEqual(result, expected_output, f'Should be {expected_output}')            

                  
  