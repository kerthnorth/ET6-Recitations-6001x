"""
Created on Fri Jan 24 11:39:16 2025
@author: Somaia

--- 2: Performing Calculations with Variables ---

Now that you’ve set up a savings variable, let’s take it a step further and use it to explore some calculations.

Imagine you’re planning to save $10 every month. How much money will you have saved in four months? Rather than working with the numbers directly, let’s use variables to perform the calculation.

Instructions
1. Create a variable called monthly_savings and assign it the value 10.
2. Define another variable, num_months, and set its value to 4.
3. Multiply monthly_savings by num_months and store the result in a variable called new_savings.
4. Finally, display the value of new_savings using the print() function.

"""
import unittest
from problem_2 import *

class TestMonthlySavings(unittest.TestCase):
  def testmonthlysaving(self):
    self.assertEqual(your_savings(10, 4), 40)
