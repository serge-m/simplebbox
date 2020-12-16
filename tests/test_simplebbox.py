#!/usr/bin/env python

"""Tests for `simplebbox` package."""

from simplebbox.array import x0y0wh_to_x0y0x1y1, x0y0x1y1_to_x0y0wh, ltwh_to_ltrb, ltrb_to_ltwh


def test_x0y0wh_to_x0y0x1y1():
    assert x0y0wh_to_x0y0x1y1([100, 200, 10, 20]) == [100, 200, 110, 220]
    assert ltwh_to_ltrb([100, 200, 10, 20]) == [100, 200, 110, 220]


def test_x0y0x1y1_to_x0y0wh():
    assert x0y0x1y1_to_x0y0wh([100, 200, 110, 220]) == [100, 200, 10, 20]
    assert ltrb_to_ltwh([100, 200, 110, 220]) == [100, 200, 10, 20]
