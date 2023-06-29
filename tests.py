import builtins
import unittest
from unittest.mock import Mock, patch
from name_finder import Names


class TestNames(unittest.TestCase):

    def setUp(self):
        self.name_finder = Names()

    def test_helper(self):
        self.assertEqual(
            self.name_finder.get_name_gender_country(
                'Chinyere'), ('Chinyere', 'Female', 'Nigeria'))
        self.assertEqual(
            self.name_finder.get_name_gender_country(
                'Phillipe'), ('Phillipe', 'Male', 'France'))


if __name__ == '__main__':
    unittest.main()
