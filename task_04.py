#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides variables for formatting."""

NEWS = 'Hi {friend}! I have {0} news! I won the raffle with number {1:0>6}!'
FNAME = 'Pat'
NTYPE = '*amazing*'
RNUM = 42



EMAIL = NEWS.format('*amazing*','42', friend='Pat')

print EMAIL

