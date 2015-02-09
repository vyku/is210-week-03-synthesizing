#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Lesson 03 Task S05."""


# Import Python libs
import unittest

# Import student file
import task_05


class L03S05TestCase(unittest.TestCase):
    """
    Tests for Lesson 03 Task S05.

    """

    def test_empty_string(self):
        """
        Tests that ``is_empty()`` returns True when passed an empty string.
        """
        self.assertTrue(task_05.is_empty(''))

    def test_nonempty_string(self):
        """
        Tests that ``is_empty()`` returns False when passed a non-empty string.
        """
        self.assertFalse(task_05.is_empty('Ni'))

    def test_nonsequence_exception(self):
        """
        Tests that ``is_empty()`` raises an exception when not passed a
        sequence object-type.
        """
        with self.assertRaises(TypeError):
            task_05.is_empty(None)
        

if __name__ == '__main__':
    unittest.main()
