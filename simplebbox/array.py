from typing import Union, List, Tuple

list_or_tuple = Union[List, Tuple]


def x0y0wh_to_x0y0x1y1(x0y0wh: list_or_tuple) -> list_or_tuple:
    """
    Converts a bounding box from format (min x, min y, width, height) to
    (min x, min y, max x, max y).
    In the coordinate system of a screen (min x, min y) corresponds to the left top corner of the box.

    >>> assert x0y0wh_to_x0y0x1y1([100, 200, 10, 20]) == [100, 200, 110, 220]
    """
    return type(x0y0wh)((
        x0y0wh[0], x0y0wh[1],
        x0y0wh[0] + x0y0wh[2], x0y0wh[1] + x0y0wh[3]
    ))


def x0y0x1y1_to_x0y0wh(x0y0x1y1: list_or_tuple) -> list_or_tuple:
    """
    Converts a bounding box from format (min x, min y, max x, max y) to
    (min x, min y, width, height).
    In the coordinate system of a screen (min x, min y) corresponds to the left top corner of the box.

    >>> assert x0y0x1y1_to_x0y0wh([100, 200, 110, 220]) == [100, 200, 10, 20]
    """
    return type(x0y0x1y1)((
        x0y0x1y1[0], x0y0x1y1[1],
        x0y0x1y1[2] - x0y0x1y1[0], x0y0x1y1[3] - x0y0x1y1[1]
    ))


ltwh_to_ltrb = x0y0wh_to_x0y0x1y1
ltrb_to_ltwh = x0y0x1y1_to_x0y0wh
