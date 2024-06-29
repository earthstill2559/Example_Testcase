from coe_number.grid_challenge import testgridChallenge
import unittest

class GridChallengeTest(unittest.TestCase):
    def test_give_text1(self):
        a = ['hoyuy', 'trstd', 'qwars', 'tfghd']
        expected_output = 'NO'
        result = testgridChallenge(a)

        self.assertEqual(result, expected_output)

    def test_give_text2(self):
        a = ['ero','ertg', 'asrt']
        expected_output = 'NO'
        result = testgridChallenge(a)

        self.assertEqual(result, expected_output)

    def test_give_text3(self):
        a = ['abe', 'adr', 'eds']
        expected_output = 'YES'
        result = testgridChallenge(a)

        self.assertEqual(result, expected_output)

    def test_give_text4(self):
        a = ['opa', 'tys', 'tra']
        expected_output = 'NO'
        result = testgridChallenge(a)

        self.assertEqual(result, expected_output)

    def test_give_text5(self):
        a = ['tops', 'rest', 'oppa']
        expected_output = 'NO'
        result = testgridChallenge(a)

        self.assertEqual(result, expected_output)

    def test_give_text6_null(self):
        a = []
        expected_output = 'Error'
        result = testgridChallenge(a)

        self.assertEqual(result, expected_output)

    def test_give_text7(self):
        a = ['asdfg', 'qwert', 'yuiop', 'bnmui', 'fghjk', 'zxcds']
        expected_output = 'NO'
        result = testgridChallenge(a)

        self.assertEqual(result, expected_output)

    def test_give_text8(self):
        a = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
        expected_output = 'YES'
        result = testgridChallenge(a)

        self.assertEqual(result, expected_output)                    