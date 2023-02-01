# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 12:10:24 2021

@author: ASUS
"""

import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(5,10), 15)
        self.assertEqual(calc.add(-1,1), 0)
        self.assertEqual(calc.add(-1,-1), -2)
        
    def test_subtract(self):
        self.assertEqual(calc.subtract(5,10), -5)
        self.assertEqual(calc.subtract(-1,1), -2)
        self.assertEqual(calc.subtract(-1,-1), 0)
        
    def test_multiplication(self):
        self.assertEqual(calc.multiplication(5,10), 50)
        self.assertEqual(calc.multiplication(-1,1), -1)
        self.assertEqual(calc.multiplication(-1,-1), 1)
        
    def test_divide(self):
        self.assertEqual(calc.divide(5,10), 0.5)
        self.assertEqual(calc.divide(-1,1), -1)
        self.assertEqual(calc.divide(-1,-1), 1)
        
        with self.assertRaises(ValueError):
            calc.divide(10,0)
            #this is done by context Manager
            
    

if __name__ == '__main__' :
    unittest.main()