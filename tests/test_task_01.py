#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 03 Task S01."""


# Import Python libs
import re
import unittest

# Import student file
import task_01


class L03S01TestCase(unittest.TestCase):
    """
    Tests for Lesson 03 Task S01.

    """

    def test_fishy(self):
        """
        Tests that the FISHY variable exists and has the correct value.
        """
        regex = re.compile('surprise')
        post_replace = regex.sub('haddock', task_01.inquisition.SPANISH)
        self.assertEqual(task_01.FISHY, post_replace)


if __name__ == '__main__':
    unittest.main()
