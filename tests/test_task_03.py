#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Lesson 03 Task S03."""


# Import Python libs
import unittest

# Import student file
import task_03


class L03S03TestCase(unittest.TestCase):
    """
    Tests for Lesson 03 Task S03.

    """

    def test_napoleon_reversed(self):
        """
        Tests that the REVERSED variable exists and has the correct value.
        """
        new_value = '.able was i ere ,i saw elba'

        self.assertEqual(task_03.REVERSED, new_value)


if __name__ == '__main__':
    unittest.main()
