import unittest
from unittest.mock import Mock, patch
from name_finder import Names

class TestNames(unittest.TestCase):
    # def test_start_program(self):
    
    def test_find_origin(self):
        # Create a mock object to simulate the user input
        input_mock = Mock()
        #input_mock.return_value = "The name Chinyere originates from Nigeria"
        Names.find_origin(self)
        #self.assertTrue(input_mock.called)
        # Run the test case
        input_mock.assert_called_with("Chinyere", "The name Chinyere originates from Nigeria")
        #self.assertEqual(Names.find_origin(), input_mock.return_value)

    # def test_find_names(self):

    # def test_baby_names(self):


if __name__ == '__main__':
    unittest.main()