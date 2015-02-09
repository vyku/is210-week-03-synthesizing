#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 03 Task S04."""


# Import Python libs
import unittest

# Import student file
import task_04


class L03S04TestCase(unittest.TestCase):
    """
    Tests for Lesson 04 Task S04.

    """

    def test_email(self):
        """
        Tests that the EMAIL variable exists and has the correct value.
        """
        email = ('Hi Pat! I have *amazing* news! I won the raffle with '
                 'number 000042!')
        self.assertEqual(task_04.EMAIL, email)

    def test_formatting_string(self):
        """
        Tests that the NEWS variable was modified properly.

        If modified correctly, other values should be possible.
        """
        email_tc = ('Hi Alex! I have drab news! I won the raffle with '
                 'number 005678!')
        email_fmt = task_04.NEWS.format('drab', 5678, friend='Alex')
        self.assertEqual(email_fmt, email_tc)
        

if __name__ == '__main__':
    unittest.main()
