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
            
