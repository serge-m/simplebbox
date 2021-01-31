#!/usr/bin/env python

"""Tests for `simplebbox` package."""
from pytest import approx

from simplebbox.array import cxcywh_to_x0y0x1y1_float


def test_cxcywh_to_x0y0x1y1_float():
    assert cxcywh_to_x0y0x1y1_float([100, 200, 10, 20]) == approx([95., 190., 105., 210.])
    assert cxcywh_to_x0y0x1y1_float([100, 200, 11, 21]) == approx([94.5, 189.5, 105.5, 210.5])
    assert cxcywh_to_x0y0x1y1_float([100., 200., 11., 21.]) == approx([94.5, 189.5, 105.5, 210.5])
    assert cxcywh_to_x0y0x1y1_float([100, 200, 10.8, 20.8]) == approx([95 - 0.4, 190 - 0.4, 105 + 0.4, 210 + 0.4])
