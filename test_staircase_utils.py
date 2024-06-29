from coe_number.staircase import staircase
import unittest

class StaircaseTest(unittest.TestCase):
    def test_give_2_with_hash(self):
        a = 2
        b = '#'
        expected_output = \
        " #\n" + \
        "##"
        result = staircase(a, b)
        self.assertEqual(result, expected_output, f'Should be {expected_output}')

    def test_give_10_with_plus(self):
        a = 10
        b = '+'
        expected_output = \
        "         +\n" + \
        "        ++\n" + \
        "       +++\n" + \
        "      ++++\n" + \
        "     +++++\n" + \
        "    ++++++\n" + \
        "   +++++++\n" + \
        "  ++++++++\n" + \
        " +++++++++\n" + \
        "++++++++++"         
        result = staircase(a, b)
        self.assertEqual(result, expected_output, f'Should be {expected_output}') 

    def test_give_4_with_star(self):
        a = 4
        b = '*'
        expected_output = \
        "   *\n" + \
        "  **\n" + \
        " ***\n" + \
        "****"
        result = staircase(a, b)
        self.assertEqual(result, expected_output, f'Should be {expected_output}')

    def test_give_20_with_dollar(self):
        a = 20
        b = '$'
        expected_output = \
        "                   $\n" + \
        "                  $$\n" + \
        "                 $$$\n" + \
        "                $$$$\n" + \
        "               $$$$$\n" + \
        "              $$$$$$\n" + \
        "             $$$$$$$\n" + \
        "            $$$$$$$$\n" + \
        "           $$$$$$$$$\n" + \
        "          $$$$$$$$$$\n" + \
        "         $$$$$$$$$$$\n" + \
        "        $$$$$$$$$$$$\n" + \
        "       $$$$$$$$$$$$$\n" + \
        "      $$$$$$$$$$$$$$\n" + \
        "     $$$$$$$$$$$$$$$\n" + \
        "    $$$$$$$$$$$$$$$$\n" + \
        "   $$$$$$$$$$$$$$$$$\n" + \
        "  $$$$$$$$$$$$$$$$$$\n" + \
        " $$$$$$$$$$$$$$$$$$$\n" + \
        "$$$$$$$$$$$$$$$$$$$$"         
        result = staircase(a, b)
        self.assertEqual(result, expected_output, f'Should be {expected_output}') 
        
    def test_give_30_with_caret(self):
        a = 30
        b = '^'
        expected_output = \
        "                             ^\n" + \
        "                            ^^\n" + \
        "                           ^^^\n" + \
        "                          ^^^^\n" + \
        "                         ^^^^^\n" + \
        "                        ^^^^^^\n" + \
        "                       ^^^^^^^\n" + \
        "                      ^^^^^^^^\n" + \
        "                     ^^^^^^^^^\n" + \
        "                    ^^^^^^^^^^\n" + \
        "                   ^^^^^^^^^^^\n" + \
        "                  ^^^^^^^^^^^^\n" + \
        "                 ^^^^^^^^^^^^^\n" + \
        "                ^^^^^^^^^^^^^^\n" + \
        "               ^^^^^^^^^^^^^^^\n" + \
        "              ^^^^^^^^^^^^^^^^\n" + \
        "             ^^^^^^^^^^^^^^^^^\n" + \
        "            ^^^^^^^^^^^^^^^^^^\n" + \
        "           ^^^^^^^^^^^^^^^^^^^\n" + \
        "          ^^^^^^^^^^^^^^^^^^^^\n" + \
        "         ^^^^^^^^^^^^^^^^^^^^^\n" + \
        "        ^^^^^^^^^^^^^^^^^^^^^^\n" + \
        "       ^^^^^^^^^^^^^^^^^^^^^^^\n" + \
        "      ^^^^^^^^^^^^^^^^^^^^^^^^\n" + \
        "     ^^^^^^^^^^^^^^^^^^^^^^^^^\n" + \
        "    ^^^^^^^^^^^^^^^^^^^^^^^^^^\n" + \
        "   ^^^^^^^^^^^^^^^^^^^^^^^^^^^\n" + \
        "  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n" + \
        " ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n" + \
        "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"         
        result = staircase(a, b)
        self.assertEqual(result, expected_output, f'Should be {expected_output}')

    def test_give_negative2_with_hash(self):
        a = -15
        b = '###'
        expected_output = 'Error: Total number of stairs must be between 1-30 '
        result = staircase(a, b)
        self.assertEqual(result, expected_output, f'Should be {expected_output}') 
    def test_give_negative2_with_notbe_creat(self):
        a = 99
        b = '$$$'
        expected_output = 'Error: Total number of stairs must be between 1-30 '
        result = staircase(a, b)
        self.assertEqual(result, expected_output, f'Should be {expected_output}')                      