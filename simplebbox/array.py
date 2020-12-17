from typing import Union, List, Tuple

list_or_tuple = Union[List, Tuple]


def x0y0wh_to_x0y0x1y1(x0y0wh: list_or_tuple) -> list_or_tuple:
    """
    Converts a bounding box from format (min x, min y, width, height) to
    (min x, min y, max x, max y). The type of the input is preserved.
    In the coordinate system of a screen (min x, min y) corresponds to the left top corner of the box.

    >>> x0y0wh_to_x0y0x1y1([100, 200, 10, 20])
    [100, 200, 110, 220]
    >>> x0y0wh_to_x0y0x1y1((100, 200, 10, 20))
    (100, 200, 110, 220)
    """
    return type(x0y0wh)((
        x0y0wh[0], x0y0wh[1],
        x0y0wh[0] + x0y0wh[2], x0y0wh[1] + x0y0wh[3]
    ))


def x0y0x1y1_to_x0y0wh(x0y0x1y1: list_or_tuple) -> list_or_tuple:
    """
    Converts a bounding box from format (min x, min y, max x, max y) to
    (min x, min y, width, height). The type of the input is preserved.
    In the coordinate system of a screen (min x, min y) corresponds to the left top corner of the box.

    >>> x0y0x1y1_to_x0y0wh([100, 200, 110, 220])
    [100, 200, 10, 20]
    >>> x0y0x1y1_to_x0y0wh((100, 200, 110, 220))
    (100, 200, 10, 20)
    """
    return type(x0y0x1y1)((
        x0y0x1y1[0], x0y0x1y1[1],
        x0y0x1y1[2] - x0y0x1y1[0], x0y0x1y1[3] - x0y0x1y1[1]
    ))


def cxcywh_to_x0y0wh_round_int(cxcywh: list_or_tuple) -> list_or_tuple:
    """
    Converts a bounding box from format (center x, center y, width, height) to
    integer (min x, min y, width, height). Floats are rounded.
    In the coordinate system of a screen (min x, min y) corresponds to the left top corner of the box.

    >>> cxcywh_to_x0y0wh_round_int([100, 200, 10, 20])
    [95, 190, 10, 20]
    >>> cxcywh_to_x0y0wh_round_int([100, 200, 11, 21])
    [94, 190, 11, 21]
    >>> cxcywh_to_x0y0wh_round_int([100., 200., 11., 21.])
    [94, 190, 11, 21]
    >>> cxcywh_to_x0y0wh_round_int([100, 200, 10.8, 21.8])
    [95, 189, 11, 22]
    >>> cxcywh_to_x0y0wh_round_int([100.5, 200.5, 10., 20.])
    [96, 190, 10, 20]
    """
    cx, cy, w, h = cxcywh
    x0 = round(cx - w / 2)
    y0 = round(cy - h / 2)
    return type(cxcywh)((
        x0,
        y0,
        round(w),
        round(h)
    ))


def cxcywh_to_x0y0wh_trunc_int(cxcywh: list_or_tuple) -> list_or_tuple:
    """
    Converts a bounding box from format (center x, center y, width, height) to
    integer (min x, min y, width, height) using only integer operations.
    In the coordinate system of a screen (min x, min y) corresponds to the left top corner of the box.

    >>> cxcywh_to_x0y0wh_trunc_int([100, 200, 10, 20])
    [95, 190, 10, 20]
    >>> cxcywh_to_x0y0wh_trunc_int([100, 200, 11, 21])
    [95, 190, 11, 21]
    >>> cxcywh_to_x0y0wh_trunc_int([100., 200., 11., 21.])
    [95, 190, 11, 21]
    >>> cxcywh_to_x0y0wh_trunc_int([100, 200, 10.8, 21.8])
    [95, 190, 10, 21]
    >>> cxcywh_to_x0y0wh_trunc_int([100.5, 200.5, 10., 20.])
    [95, 190, 10, 20]
    """
    cx, cy, w, h = cxcywh
    x0 = cx - w // 2
    y0 = cy - h // 2
    return type(cxcywh)((
        int(x0),
        int(y0),
        int(w),
        int(h)
    ))


def cxcywh_to_x0y0wh_float(cxcywh: list_or_tuple) -> list_or_tuple:
    """
    Converts a bounding box from format (center x, center y, width, height) to
    float (min x, min y, width, height).
    In the coordinate system of a screen (min x, min y) corresponds to the left top corner of the box.
    """

    return type(cxcywh)((
        cxcywh[0] - cxcywh[2] / 2.0,
        cxcywh[1] - cxcywh[3] / 2.0,
        float(cxcywh[2]),
        float(cxcywh[3])
    ))


def cxcywh_to_x0y0x1y1_round_int(cxcywh: list_or_tuple) -> list_or_tuple:
    """
    Converts a bounding box from format (center x, center y, width, height) to
    integer (min x, min y, max x, max y). Floats are rounded.
    In the coordinate system of a screen (min x, min y) corresponds to the left top corner of the box.

    >>> cxcywh_to_x0y0x1y1_round_int([100, 200, 10, 20])
    [95, 190, 105, 210]
    >>> cxcywh_to_x0y0x1y1_round_int([100, 200, 11, 21])
    [94, 190, 105, 211]
    >>> cxcywh_to_x0y0x1y1_round_int([100., 200., 11., 21.])
    [94, 190, 105, 211]
    >>> cxcywh_to_x0y0x1y1_round_int([100, 200, 10.8, 21.8])
    [95, 189, 106, 211]
    >>> cxcywh_to_x0y0x1y1_round_int([100.5, 200.5, 10., 20.])
    [96, 190, 106, 210]
    """
    cx, cy, w, h = cxcywh
    x0 = round(cx - w / 2)
    y0 = round(cy - h / 2)
    return type(cxcywh)((
        x0,
        y0,
        x0 + round(w),
        y0 + round(h)
    ))


def cxcywh_to_x0y0x1y1_trunc_int(cxcywh: list_or_tuple) -> list_or_tuple:
    """
    Converts a bounding box from format (center x, center y, width, height) to
    integer (min x, min y, max x, max y) using only integer operations.
    In the coordinate system of a screen (min x, min y) corresponds to the left top corner of the box.

    >>> cxcywh_to_x0y0x1y1_trunc_int([100, 200, 10, 20])
    [95, 190, 105, 210]
    >>> cxcywh_to_x0y0x1y1_trunc_int([100, 200, 11, 21])
    [95, 190, 106, 211]
    >>> cxcywh_to_x0y0x1y1_trunc_int([100., 200., 11., 21.])
    [95, 190, 106, 211]
    >>> cxcywh_to_x0y0x1y1_trunc_int([100, 200, 10.8, 21.8])
    [95, 190, 105, 211]
    >>> cxcywh_to_x0y0x1y1_trunc_int([100.5, 200.5, 10., 20.])
    [95, 190, 105, 210]
    """
    cx, cy, w, h = cxcywh
    x0 = cx - w // 2
    y0 = cy - h // 2
    return type(cxcywh)((
        int(x0),
        int(y0),
        int(x0 + w),
        int(y0 + h)
    ))


def cxcywh_to_x0y0x1y1_float(cxcywh: list_or_tuple) -> list_or_tuple:
    """
    Converts a bounding box from format (center x, center y, width, height) to
    float (min x, min y, max x, max y).
    In the coordinate system of a screen (min x, min y) corresponds to the left top corner of the box.
    """
    cx, cy, w, h = cxcywh
    x0 = cx - w / 2.
    y0 = cy - h / 2.
    return type(cxcywh)((
        x0,
        y0,
        float(x0 + w),
        float(y0 + h)
    ))
