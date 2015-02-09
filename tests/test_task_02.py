#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Lesson 03 Task S02."""


# Import Python libs
import unittest

# Import student file
import inquisition
import task_02


class L03S02TestCase(unittest.TestCase):
    """
    Tests for Lesson 03 Task S02.

    """

    def test_flemish(self):
        """
        Tests that the FLEMISH variable exists and has the correct value.
        """
        post_replace = inquisition.SPANISH.replace('Spanish', 'Flemish', 1)
        self.assertEqual(task_02.FLEMISH, post_replace)


if __name__ == '__main__':
    unittest.main()
