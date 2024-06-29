import unittest
from coe_number.cat_and_mouse import catAndMouse

class CatandMouseTest(unittest.TestCase):
    def test_give_cata1_catb2_mousec3(self):
        catA = 1
        catB = 2
        mouseC = 3
        expected_output = 'Cat B'

        result = catAndMouse(catA,catB,mouseC)
        self.assertEqual(result, expected_output, f'Should be {expected_output}')

    def test_give_cata5_catb6_mousec8(self):
        catA = 5
        catB = 6
        mouseC = 8
        expected_output = 'Cat B'

        result = catAndMouse(catA,catB,mouseC)
        self.assertEqual(result, expected_output, f'Should be {expected_output}')  

    def test_give_cata3_catb5_mousec4(self):
        catA = 3
        catB = 5
        mouseC = 4
        expected_output = 'Mouse C'

        result = catAndMouse(catA,catB,mouseC)
        self.assertEqual(result, expected_output, f'Should be {expected_output}')   

    def test_give_cata4_catb11_mousec5(self):
        catA = 4
        catB = 11
        mouseC = 5
        expected_output = 'Cat A'

        result = catAndMouse(catA,catB,mouseC)
        self.assertEqual(result, expected_output, f'Should be {expected_output}')  
        
    def test_give_cata111_catb46_mousec10(self):
        catA = 111
        catB = 46
        mouseC = 10
        expected_output = 'Error'

        result = catAndMouse(catA,catB,mouseC)
        self.assertEqual(result, expected_output, f'Should be {expected_output}')

    def test_give_cata10_catb10_mousec10(self):
        catA = 10
        catB = 10
        mouseC = 10
        expected_output = 'Mouse C'

        result = catAndMouse(catA,catB,mouseC)
        self.assertEqual(result, expected_output, f'Should be {expected_output}')  

    def test_give_cata110_catb120_mousec130(self):
        catA = 110
        catB = 120
        mouseC = 130
        expected_output = 'Error'

        result = catAndMouse(catA,catB,mouseC)
        self.assertEqual(result, expected_output, f'Should be {expected_output}')                