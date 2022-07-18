#!/usr/bin/env python3
""" python for unittesting """

import unittest
from parameterized import parameterized
import utils


class TestAccessNestedMap(unittest.TestCase):
    """ access nested map testing """
    
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(self, a, b, c):
        """ test access function """ 
        res = utils.access_nested_map(a, b)
        self.assertEqual(res, c)
    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
        ])
    def test_access_nested_map_exception(self, a, b):
        """ test access nested map  excep """
        with self.assertRaises(KeyError):
            utils.access_nested_map(a, b)

