import unittest
from main import convert_name, math_computation


class TestHelperMethods(unittest.TestCase):

    # convert_name() tests

    def test_male_name(self):
        self.assertEqual(convert_name('harry','potter','m'), 'Mr. Harry Potter')

    def test_female_name(self):
        self.assertEqual(convert_name('hermione','granger','f'), 'Ms. Hermione Granger')

    def test_genderqueer_name(self):
        self.assertEqual(convert_name('chris','jones',''), 'Mx. Chris Jones')


    # math_computation() tests

    def test_add(self):
        self.assertEqual(math_computation(4,7,'add'), 11)

    def test_subtract(self):
        self.assertEqual(math_computation(12,9,'subtract'), 3)

    def test_multiply(self):
        self.assertEqual(math_computation(4,7,'multiply'), 28)

    def test_divide(self):
        self.assertEqual(math_computation(5,2,'divide'), 2.5)

if __name__ == '__main__':
    unittest.main()
