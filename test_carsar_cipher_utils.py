from coe_number.caesar_cipher import create_caesar_cipher
import unittest

class CaesarCipherTest(unittest.TestCase):
    def test_give_dsdsfewff_rotated_by_2(self):
        Text = 'dsdsfewff'
        k = 2
        expected_output = 'fufuhgyhh'

        result = create_caesar_cipher(Text, k)

        self.assertEqual(result, expected_output, f'Should be {expected_output}')

    def test_give_HFREGDFhtgf_rotated_by_5(self):
        Text = 'HFREGDFhtgf'
        b = 5
        expected_output = 'MKWJLIKmylk'

        result = create_caesar_cipher(Text, b)

        self.assertEqual(result, expected_output, f'Should be {expected_output}')

    def test_give_Iaminlove_rotated_by_50(self):
        Text = 'Iaminlove'
        b = 50
        expected_output = 'Gykgljmtc'

        result = create_caesar_cipher(Text, b)

        self.assertEqual(result, expected_output, f'Should be {expected_output}')  

    def test_give_null_rotated_by_10_Error(self):
        Text = ''
        b = 10
        expected_output = 'Error'

        result = create_caesar_cipher(Text, b)

        self.assertEqual(result, expected_output, f'Should be {expected_output}')

    def test_give_Darari_rotated_by_120_Error(self):
        Text = 'Darari'
        b = 120
        expected_output = 'Error'

        result = create_caesar_cipher(Text, b)

        self.assertEqual(result, expected_output, f'Should be {expected_output}')   

    def test_give_BringMe_rotated_by_negative_10_Error(self):
        Text = 'EaRthzI'
        b = -10
        expected_output = 'Error'

        result = create_caesar_cipher(Text, b)

        self.assertEqual(result, expected_output, f'Should be {expected_output}')

    def test_give_BringMe_rotated_by_negative_15(self):
        Text = 'Noppadon'
        b = 15
        expected_output = 'Cdeepsdc'

        result = create_caesar_cipher(Text, b)

        self.assertEqual(result, expected_output, f'Should be {expected_output}')                      