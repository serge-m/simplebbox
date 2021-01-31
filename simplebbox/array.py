from typing import Union, List, Tuple

float_or_int = Union[float, int]
list_or_tuple = Union[List, Tuple]
pair = Union[
    List[float_or_int],
    Tuple[float_or_int]
]


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


def cxcywh_to_x0y0wh(cxcywh: list_or_tuple, convert_fn=lambda x: x) -> list_or_tuple:
    """
    Converts a bounding box from format
    (center x, center y, width, height) to
    (min x, min y, width, height).

    Rounding function can be used as `convert_fn` to get integer results instead of float.
    In the coordinate system of a screen (min x, min y) corresponds to the left top corner of the box.

    >>> cxcywh_to_x0y0wh([100, 200, 10, 20], convert_fn=round)
    [95, 190, 10, 20]
    >>> cxcywh_to_x0y0wh([100, 200, 11, 21], convert_fn=round)
    [94, 190, 11, 21]
    >>> cxcywh_to_x0y0wh([100., 200., 11., 21.], convert_fn=round)
    [94, 190, 11, 21]
    >>> cxcywh_to_x0y0wh([100, 200, 10.8, 21.8], convert_fn=round)
    [95, 189, 11, 22]
    >>> cxcywh_to_x0y0wh([100.5, 200.5, 10., 20.], convert_fn=round)
    [96, 190, 10, 20]
    """
    cx, cy, w, h = cxcywh
    x0 = cx - w / 2
    y0 = cy - h / 2
    return type(cxcywh)((
        convert_fn(x0),
        convert_fn(y0),
        convert_fn(w),
        convert_fn(h)
    ))


def cxcywh_to_x0y0wh_int_div(cxcywh: list_or_tuple, convert_fn=lambda x: x) -> list_or_tuple:
    """
    Converts a bounding box from format
    (center x, center y, width, height) to
    (min x, min y, width, height)
    using integer operations (division).

    Type conversion function `convert_fn` can be used to get results as floats.

    In the coordinate system of a screen (min x, min y) corresponds to the left top corner of the box.

    >>> cxcywh_to_x0y0wh_int_div([100, 200, 10, 20])
    [95, 190, 10, 20]
    >>> cxcywh_to_x0y0wh_int_div([100, 200, 11, 21])
    [95, 190, 11, 21]
    >>> cxcywh_to_x0y0wh_int_div([100., 200., 11., 21.])
    [95.0, 190.0, 11.0, 21.0]
    >>> cxcywh_to_x0y0wh_int_div([100., 200., 11., 21.], int)
    [95, 190, 11, 21]
    """
    cx, cy, w, h = cxcywh
    x0 = cx - w // 2
    y0 = cy - h // 2
    return type(cxcywh)((
        convert_fn(x0),
        convert_fn(y0),
        convert_fn(w),
        convert_fn(h)
    ))


def cxcywh_to_x0y0x1y1(cxcywh: list_or_tuple, convert_fn=lambda x: x) -> list_or_tuple:
    """
    Converts a bounding box from format (center x, center y, width, height) to
    integer (min x, min y, max x, max y). Floats are rounded.
    In the coordinate system of a screen (min x, min y) corresponds to the left top corner of the box.

    >>> cxcywh_to_x0y0x1y1([100, 200, 10, 20], convert_fn=round)
    [95, 190, 105, 210]
    >>> cxcywh_to_x0y0x1y1([100, 200, 11, 21], convert_fn=round)
    [94, 190, 105, 211]
    >>> cxcywh_to_x0y0x1y1([100., 200., 11., 21.], convert_fn=round)
    [94, 190, 105, 211]
    >>> cxcywh_to_x0y0x1y1([100, 200, 10.8, 21.8], convert_fn=round)
    [95, 189, 106, 211]
    >>> cxcywh_to_x0y0x1y1([100.5, 200.5, 10., 20.], convert_fn=round)
    [96, 190, 106, 210]
    """
    cx, cy, w, h = cxcywh
    x0 = convert_fn(cx - w / 2)
    y0 = convert_fn(cy - h / 2)
    return type(cxcywh)((
        x0,
        y0,
        convert_fn(x0 + w),
        convert_fn(y0 + h)
    ))


def cxcywh_to_x0y0x1y1_int_div(cxcywh: list_or_tuple, convert_fn=lambda x: x) -> list_or_tuple:
    """
    Converts a bounding box from format
    (center x, center y, width, height) to
    (min x, min y, max x, max y)
    using integer operations (division).

    In the coordinate system of a screen (min x, min y) corresponds to the left top corner of the box.

    >>> cxcywh_to_x0y0x1y1_int_div([100, 200, 10, 20])
    [95, 190, 105, 210]
    >>> cxcywh_to_x0y0x1y1_int_div([100, 200, 11, 21])
    [95, 190, 106, 211]
    >>> cxcywh_to_x0y0x1y1_int_div([100., 200., 11., 21.], int)
    [95, 190, 106, 211]
    >>> cxcywh_to_x0y0x1y1_int_div([100, 200, 10.8, 21.8], int)
    [95, 190, 105, 211]
    >>> cxcywh_to_x0y0x1y1_int_div([100.5, 200.5, 10., 20.], int)
    [95, 190, 105, 210]
    """
    cx, cy, w, h = cxcywh
    x0 = convert_fn(cx - w // 2)
    y0 = convert_fn(cy - h // 2)
    return type(cxcywh)((
        x0,
        y0,
        convert_fn(x0 + w),
        convert_fn(y0 + h)
    ))


def xyxy_abs_to_rel(xyxy: list_or_tuple, image_wh: pair) -> list_or_tuple:
    """
    Converts a bounding box from format (x, y, width, height) or (x, y, x, y) from absolute to relative values
    with respect to image width and height.

    Parameters
    ----------
    image_wh : tuple of width and height of image

    >>> xyxy_abs_to_rel([100, 200, 200, 50], [400, 200])
    [0.25, 1.0, 0.5, 0.25]
    """
    x0, y0, x1, y1 = xyxy
    w, h = image_wh
    return type(xyxy)((
        x0 / w, y0 / h,
        x1 / w, y1 / h
    ))


def xyxy_rel_to_abs_int(xyxy: list_or_tuple, image_wh: pair) -> list_or_tuple:
    """
    Converts a bounding box from format (x, y, width, height) or (x, y, x, y) from relative to absolute values
    with respect to image width and height.

    Parameters
    ----------
    xyxy : tuple or list. (x, y, width, height) or (x, y, x, y).
    image_wh : tuple of width and height of image

    >>> xyxy_rel_to_abs_int([0.25, 1.0, 0.5, 0.25], [400, 200])
    [100, 200, 200, 50]
    """
    x0, y0, x1, y1 = xyxy
    w, h = image_wh
    return type(xyxy)((
        int(x0 * w), int(y0 * h),
        int(x1 * w), int(y1 * h)
    ))
