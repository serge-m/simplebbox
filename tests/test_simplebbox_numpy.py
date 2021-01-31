#!/usr/bin/env python

"""Tests for `simplebbox` package."""
import numpy as np
import torch
from pytest import approx

from simplebbox.numpy_array import bbox_numpy
from simplebbox.torch_tensor import bbox_torch


class equal_np_array:
    # Tell numpy to use our `__eq__` operator instead of its.
    __array_ufunc__ = None
    __array_priority__ = 100

    def __init__(self, *args, **kwargs):
        self.value = np.array(*args, **kwargs)

    def __repr__(self):
        return repr(self.value)

    def __eq__(self, other):
        if not isinstance(other, np.ndarray):
            return False
        return np.array_equal(self.value, other)


class equal_tensor:
    __array_ufunc__ = None
    __array_priority__ = 100

    def __init__(self, *args, **kwargs):
        self.value = torch.tensor(*args, **kwargs)

    def __repr__(self):
        return repr(self.value)

    def __eq__(self, other):
        if not isinstance(other, torch.Tensor):
            return False
        return torch.equal(self.value, other)


def test_x0y0wh_to_x0y0x1y1():
    in1 = [100, 200, 10, 20]
    out1 = [100, 200, 110, 220]
    in2 = [10, 20, 10, 20]
    out2 = [10, 20, 20, 40]

    assert bbox_numpy.x0y0wh_to_x0y0x1y1(np.array(in1)) == equal_np_array(out1, dtype='int')
    assert bbox_numpy.x0y0wh_to_x0y0x1y1(np.array([in1])) == equal_np_array([out1], dtype='int')
    assert bbox_numpy.x0y0wh_to_x0y0x1y1(np.array([in1, in2])) == equal_np_array([out1, out2], dtype='int')
    assert bbox_numpy.x0y0wh_to_x0y0x1y1(np.array([[in1, in2]])) == equal_np_array([[out1, out2]], dtype='int')

    assert bbox_torch.x0y0wh_to_x0y0x1y1(torch.tensor(in1)) == equal_tensor(out1, dtype=torch.long)
    assert bbox_torch.x0y0wh_to_x0y0x1y1(torch.tensor([in1])) == equal_tensor([out1], dtype=torch.long)
    assert bbox_torch.x0y0wh_to_x0y0x1y1(torch.tensor([in1, in2])) == equal_tensor([out1, out2], dtype=torch.long)
    assert bbox_torch.x0y0wh_to_x0y0x1y1(torch.tensor([[in1, in2]])) == equal_tensor([[out1, out2]], dtype=torch.long)


def test_x0y0x1y1_to_x0y0wh():
    in1 = [100, 200, 110, 220]
    out1 = [100, 200, 10, 20]
    in2 = [10, 20, 20, 40]
    out2 = [10, 20, 10, 20]

    assert bbox_numpy.x0y0x1y1_to_x0y0wh(np.array(in1)) == equal_np_array(out1, dtype='int')
    assert bbox_numpy.x0y0x1y1_to_x0y0wh(np.array([in1])) == equal_np_array([out1], dtype='int')
    assert bbox_numpy.x0y0x1y1_to_x0y0wh(np.array([in1, in2])) == equal_np_array([out1, out2], dtype='int')
    assert bbox_numpy.x0y0x1y1_to_x0y0wh(np.array([[in1, in2]])) == equal_np_array([[out1, out2]], dtype='int')

    assert bbox_torch.x0y0x1y1_to_x0y0wh(torch.tensor(in1)) == equal_tensor(out1, dtype=torch.long)
    assert bbox_torch.x0y0x1y1_to_x0y0wh(torch.tensor([in1])) == equal_tensor([out1], dtype=torch.long)
    assert bbox_torch.x0y0x1y1_to_x0y0wh(torch.tensor([in1, in2])) == equal_tensor([out1, out2], dtype=torch.long)
    assert bbox_torch.x0y0x1y1_to_x0y0wh(torch.tensor([[in1, in2]])) == equal_tensor([[out1, out2]], dtype=torch.long)


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