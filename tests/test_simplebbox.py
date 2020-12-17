#!/usr/bin/env python

"""Tests for `simplebbox` package."""
from pytest import approx

from simplebbox.array import x0y0wh_to_x0y0x1y1, x0y0x1y1_to_x0y0wh, \
    cxcywh_to_x0y0wh_trunc_int, \
    cxcywh_to_x0y0wh_float, \
    cxcywh_to_x0y0x1y1_float


def test_x0y0wh_to_x0y0x1y1():
    assert x0y0wh_to_x0y0x1y1([100, 200, 10, 20]) == [100, 200, 110, 220]


def test_x0y0x1y1_to_x0y0wh():
    assert x0y0x1y1_to_x0y0wh([100, 200, 110, 220]) == [100, 200, 10, 20]


def test_cxcywh_to_x0y0wh_int():
    result = cxcywh_to_x0y0wh_trunc_int([100, 200, 10.9, 21.])
    assert result == [95, 190, 10, 21]


def test_cxcywh_to_x0y0wh_float():
    assert cxcywh_to_x0y0wh_float([100, 200, 10, 20]) == approx([95., 190., 10., 20.])
    assert cxcywh_to_x0y0wh_float([100, 200, 11, 21]) == approx([94.5, 189.5, 11., 21.])
    assert cxcywh_to_x0y0wh_float([100., 200., 11., 21.]) == approx([94.5, 189.5, 11., 21.])
    assert cxcywh_to_x0y0wh_float([100, 200, 10.8, 20.8]) == approx([94.6, 189.6, 10.8, 20.8])


def test_cxcywh_to_x0y0x1y1_float():
    assert cxcywh_to_x0y0x1y1_float([100, 200, 10, 20]) == approx([95., 190., 105., 210.])
    assert cxcywh_to_x0y0x1y1_float([100, 200, 11, 21]) == approx([94.5, 189.5, 105.5, 210.5])
    assert cxcywh_to_x0y0x1y1_float([100., 200., 11., 21.]) == approx([94.5, 189.5, 105.5, 210.5])
    assert cxcywh_to_x0y0x1y1_float([100, 200, 10.8, 20.8]) == approx([95 - 0.4, 190 - 0.4, 105 + 0.4, 210 + 0.4])
