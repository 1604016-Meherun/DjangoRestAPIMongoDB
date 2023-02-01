# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 17:41:35 2021

@author: ASUS
"""

import unittest
from unittest.mock import patch
from mocking import Employee


class TestEmpoyee(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('setupClass')
        
    @classmethod
    def tearDownClass(cls):
        print('teardownclass')
    
    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Corey','Schafeer', 50000)
        self.emp_2 = Employee('Sue','Smith', 60000)
        

    def tearDown(self):
        print('testDown\n')
    
    def test_email(self):
        print('test_email')
        self.emp_1 = Employee('Corey','Schafeer', 50000)
        self.emp_2 = Employee('Sue','Smith', 60000)
        
        self.assertEqual(self.emp_1.email, 'Corey.Schafeer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')
        
        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'
        
        self.assertEqual(self.emp_1.email, 'John.Schafeer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')
        
    def test_fullname(self):
        print('test_fullname')
        self.emp_1 = Employee('Corey','Schafeer', 50000)
        self.emp_2 = Employee('Sue','Smith', 60000)
        
        self.assertEqual(self.emp_1.fullname, 'Corey Schafeer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')
        
        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'
        
        self.assertEqual(self.emp_1.fullname, 'John Schafeer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')
        
    def test_apply_raise(self):
        print('test_pay')
        self.emp_1 = Employee('Corey','Schafeer', 50000)
        self.emp_2 = Employee('Sue','Smith', 60000)
        
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
        
        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)
        
    def test_monthly_schedule(self):
        print('monthly _API')
        with patch('mocking.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'
            
            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Schafeer/May')
            self.assertEqual(schedule, 'Success')
            
            mocked_get.return_value.ok = False
            
            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEqual(schedule, 'Bad Response!')
            
if __name__ == '__main__':
     unittest.main()
        
        