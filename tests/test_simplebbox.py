#!/usr/bin/env python

"""Tests for `simplebbox` package."""

import pytest


from simplebbox.simplebbox import *


def test_content(response):
    assert ltwh_to_ltrb([100, 200, 10, 20]) == [100, 200, 110, 220]
