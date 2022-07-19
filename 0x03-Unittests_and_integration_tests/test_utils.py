#!/usr/bin/env python3
""" python for unittesting """

from unittest import TestCase, mock
from parameterized import parameterized
import utils
import json
import requests


class TestAccessNestedMap(TestCase):
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

class TestGetJson(TestCase):
    """ test class for get json method """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    def test_get_json(self, a, b):
        """ test the json """
        with mock.patch('utils.requests.get') as mget:
            payload = {"test_url": a, "test_payload": b} 
            mget.return_value.json.return_value = json.dumps(payload)
            res = utils.get_json(a)
            self.assertEqual(res, json.dumps(payload))
           

class TestMemoize(TestCase):
    """ Class for testing memoization """

    def test_memoize(self):
        """ Tests memoize function """

        class TestClass:
            """ Test class """

            def a_method(self):
                """ Method to always return 42 """
                return 42

            @utils.memoize
            def a_property(self):
                """ Returns memoized property """
                return self.a_method()

        with mock.patch.object(TestClass, 'a_method', return_value=42) as patched:
            test_class = TestClass()
            real_return = test_class.a_property
            real_return = test_class.a_property

            self.assertEqual(real_return, 42)
            patched.assert_called_once()
