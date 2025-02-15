"""
This program tests if we can successfully store variables.
"""

import unittest
from problem_1 import saved_variable

class TestVariableStorage(unittest.TestCase):
    def test_variable_storage(self):
        self.assertEqual(saved_variable(100), 100)

if __name__ == "__main__":
    unittest.main()
