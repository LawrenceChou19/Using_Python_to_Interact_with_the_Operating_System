#!/usr/bin/env python3

from rearrange import rearrange_name
import unittest
class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase),expected)#self.assertEqual to compare the expected and result is the same or not

    def test_empty(self):#TypeError: 'NoneType' object is not subscriptable
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase),expected)
    
    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase),expected)
    
    def test_one_name(self):
        testcase = "Voltaire"
        expected = "Voltaire"
        self.assertEqual(rearrange_name(testcase),expected)

unittest.main()

