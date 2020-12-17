import numpy as np

__all__ = ["ltrb_to_ltwh", "ltwh_to_ltrb", "x0y0x1y1_to_x0y0wh", "x0y0wh_to_x0y0x1y1"]


def x0y0wh_to_x0y0x1y1(x0y0wh: np.ndarray) -> np.ndarray:
    """
    Converts a bounding box from format (min x, min y, width, height) to
    (min x, min y, max x, max y).
    In the coordinate system of a screen (min x, min y) corresponds to the left top corner of the box.

    >>> x0y0x1y1 = x0y0wh_to_x0y0x1y1(np.array([100, 200, 10, 20]))
    >>> np.array_equal(x0y0x1y1, [100, 200, 110, 220])
    True
    """
    return np.asarray([
        x0y0wh[0], x0y0wh[1],
        x0y0wh[0] + x0y0wh[2], x0y0wh[1] + x0y0wh[3]
    ], dtype=x0y0wh.dtype)


def x0y0x1y1_to_x0y0wh(x0y0x1y1: np.ndarray) -> np.ndarray:
    """
    Converts a bounding box from format (min x, min y, max x, max y) to
    (min x, min y, width, height).
    In the coordinate system of a screen (min x, min y) corresponds to the left top corner of the box.

    >>> x0y0wh = x0y0x1y1_to_x0y0wh(np.array([100, 200, 110, 220]))
    >>> np.array_equal(x0y0wh, [100, 200, 10, 20])
    True
    """
    return np.asarray((
        x0y0x1y1[0], x0y0x1y1[1],
        x0y0x1y1[2] - x0y0x1y1[0], x0y0x1y1[3] - x0y0x1y1[1]
    ), dtype=x0y0x1y1.dtype)


ltwh_to_ltrb = x0y0wh_to_x0y0x1y1
ltrb_to_ltwh = x0y0x1y1_to_x0y0wh
