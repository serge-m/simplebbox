def atleast_2d(x):
    if x.ndim == 1:
        return x.reshape(1, *x.shape)
    return x


class ArrayProcessor:
    def __init__(self, stack_fn):
        self.stack = stack_fn

    def x0y0wh_to_x0y0x1y1(self, x0y0wh):
        """
        Converts a bounding box from format
        (min x, min y, width, height) to
        (min x, min y, max x, max y).
        In the coordinate system of a screen (min x, min y) corresponds to the left top corner of the box.
        """
        arr = atleast_2d(x0y0wh)
        res = [
            arr[..., 0], arr[..., 1],
            arr[..., 0] + arr[..., 2], arr[..., 1] + arr[..., 3]
        ]
        return self.stack(res).reshape(*x0y0wh.shape[:-1], len(res))

    def x0y0x1y1_to_x0y0wh(self, x0y0x1y1):
        """
        Converts a bounding box from format
        (min x, min y, max x, max y) to
        (min x, min y, width, height).
        In the coordinate system of a screen (min x, min y) corresponds to the left top corner of the box.
        """
        arr = atleast_2d(x0y0x1y1)
        res = [
            arr[..., 0], arr[..., 1],
            arr[..., 2] - arr[..., 0], arr[..., 3] - arr[..., 1]
        ]
        return self.stack(res).reshape(*x0y0x1y1.shape[:-1], len(res))


# def cxcywh_to_x0y0wh_round_int(cxcywh: np.ndarray, dtype=np.int) -> np.ndarray:
#     """
#     Converts a bounding box from format (center x, center y, width, height) to
#     integer (min x, min y, width, height). Floats are rounded.
#     In the coordinate system of a screen (min x, min y) corresponds to the left top corner of the box.
#
#     >>> res = cxcywh_to_x0y0wh_round_int(np.array([100, 200, 10, 20]))
#     >>> np.array_equal(res, [95, 190, 10, 20])
#     True
#     >>> res = cxcywh_to_x0y0wh_round_int(np.array([100, 200, 11, 21]))
#     >>> np.array_equal(res, [94, 190, 11, 21])
#     True
#     >>> res = cxcywh_to_x0y0wh_round_int(np.array([100., 200., 11., 21.]))
#     >>> np.array_equal(res, [94, 190, 11, 21])
#     True
#     >>> res = cxcywh_to_x0y0wh_round_int(np.array([100, 200, 10.8, 21.8]))
#     >>> np.array_equal(res, [95, 189, 11, 22])
#     True
#     >>> res = cxcywh_to_x0y0wh_round_int(np.array([100.5, 200.5, 10., 20.]))
#     >>> np.array_equal(res, [96, 190, 10, 20])
#     True
#     >>> res = cxcywh_to_x0y0wh_round_int(np.array([[100.5, 200.5, 10., 20.]]).T)
#     >>> np.array_equal(res, np.array([[96, 190, 10, 20]]).T)
#     True
#     >>> res = cxcywh_to_x0y0wh_round_int(np.array([
#     ...     [100, 200, 10, 20],
#     ...     [100, 200, 11, 21]
#     ... ]).T)
#     >>> np.array_equal(res, np.array([
#     ...     [95, 190, 10, 20],
#     ...     [94, 190, 11, 21],
#     ... ]).T)
#     True
#     """
#     assert np.issubdtype(dtype, np.integer)
#     cx, cy, w, h = cxcywh
#     x0 = np.around(cx - w / 2)
#     y0 = np.around(cy - h / 2)
#     return np.asarray((
#         x0,
#         y0,
#         np.around(w),
#         np.around(h)
#     ), dtype=dtype)
#
#
# def cxcywh_to_x0y0wh_trunc_int(cxcywh: np.ndarray, dtype=np.int) -> np.ndarray:
#     """
#     Converts a bounding box from format (center x, center y, width, height) to
#     integer (min x, min y, width, height) using only integer operations.
#     In the coordinate system of a screen (min x, min y) corresponds to the left top corner of the box.
#
#     >>> cxcywh_to_x0y0wh_trunc_int([100, 200, 10, 20])
#     [95, 190, 10, 20]
#     >>> cxcywh_to_x0y0wh_trunc_int([100, 200, 11, 21])
#     [95, 190, 11, 21]
#     >>> cxcywh_to_x0y0wh_trunc_int([100., 200., 11., 21.])
#     [95, 190, 11, 21]
#     >>> cxcywh_to_x0y0wh_trunc_int([100, 200, 10.8, 21.8])
#     [95, 190, 10, 21]
#     >>> cxcywh_to_x0y0wh_trunc_int([100.5, 200.5, 10., 20.])
#     [95, 190, 10, 20]
#     """
#     assert dtype.is_integer()
#     cx, cy, w, h = cxcywh
#     x0 = cx - w // 2
#     y0 = cy - h // 2
#     return np.asarray((
#         x0,
#         y0,
#         w,
#         h
#     ), dtype=dtype)
#
#
# def cxcywh_to_x0y0wh_float(cxcywh: np.ndarray) -> np.ndarray:
#     """
#     Converts a bounding box from format (center x, center y, width, height) to
#     float (min x, min y, width, height).
#     In the coordinate system of a screen (min x, min y) corresponds to the left top corner of the box.
#     """
#
#     return type(cxcywh)((
#         cxcywh[0] - cxcywh[2] / 2.0,
#         cxcywh[1] - cxcywh[3] / 2.0,
#         float(cxcywh[2]),
#         float(cxcywh[3])
#     ))
#
#
# def cxcywh_to_x0y0x1y1_round_int(cxcywh: np.ndarray) -> np.ndarray:
#     """
#     Converts a bounding box from format (center x, center y, width, height) to
#     integer (min x, min y, max x, max y). Floats are rounded.
#     In the coordinate system of a screen (min x, min y) corresponds to the left top corner of the box.
#
#     >>> cxcywh_to_x0y0x1y1_round_int([100, 200, 10, 20])
#     [95, 190, 105, 210]
#     >>> cxcywh_to_x0y0x1y1_round_int([100, 200, 11, 21])
#     [94, 190, 105, 211]
#     >>> cxcywh_to_x0y0x1y1_round_int([100., 200., 11., 21.])
#     [94, 190, 105, 211]
#     >>> cxcywh_to_x0y0x1y1_round_int([100, 200, 10.8, 21.8])
#     [95, 189, 106, 211]
#     >>> cxcywh_to_x0y0x1y1_round_int([100.5, 200.5, 10., 20.])
#     [96, 190, 106, 210]
#     """
#     cx, cy, w, h = cxcywh
#     x0 = round(cx - w / 2)
#     y0 = round(cy - h / 2)
#     return type(cxcywh)((
#         x0,
#         y0,
#         x0 + round(w),
#         y0 + round(h)
#     ))
#
#
# def cxcywh_to_x0y0x1y1_trunc_int(cxcywh: np.ndarray) -> np.ndarray:
#     """
#     Converts a bounding box from format (center x, center y, width, height) to
#     integer (min x, min y, max x, max y) using only integer operations.
#     In the coordinate system of a screen (min x, min y) corresponds to the left top corner of the box.
#
#     >>> cxcywh_to_x0y0x1y1_trunc_int([100, 200, 10, 20])
#     [95, 190, 105, 210]
#     >>> cxcywh_to_x0y0x1y1_trunc_int([100, 200, 11, 21])
#     [95, 190, 106, 211]
#     >>> cxcywh_to_x0y0x1y1_trunc_int([100., 200., 11., 21.])
#     [95, 190, 106, 211]
#     >>> cxcywh_to_x0y0x1y1_trunc_int([100, 200, 10.8, 21.8])
#     [95, 190, 105, 211]
#     >>> cxcywh_to_x0y0x1y1_trunc_int([100.5, 200.5, 10., 20.])
#     [95, 190, 105, 210]
#     """
#     cx, cy, w, h = cxcywh
#     x0 = cx - w // 2
#     y0 = cy - h // 2
#     return type(cxcywh)((
#         int(x0),
#         int(y0),
#         int(x0 + w),
#         int(y0 + h)
#     ))
#
#
# def cxcywh_to_x0y0x1y1_float(cxcywh: np.ndarray) -> np.ndarray:
#     """
#     Converts a bounding box from format (center x, center y, width, height) to
#     float (min x, min y, max x, max y).
#     In the coordinate system of a screen (min x, min y) corresponds to the left top corner of the box.
#     """
#     cx, cy, w, h = cxcywh
#     x0 = cx - w / 2.
#     y0 = cy - h / 2.
#     return type(cxcywh)((
#         x0,
#         y0,
#         float(x0 + w),
#         float(y0 + h)
#     ))
#
#
# def xyxy_abs_to_rel(xyxy: np.ndarray, image_wh: np.ndarray) -> np.ndarray:
#     """
#     Converts a bounding box from format (x, y, width, height) or (x, y, x, y) from absolute to relative values
#     with respect to image width and height.
#
#     Parameters
#     ----------
#     image_wh : tuple of width and height of image
#
#     >>> xyxy_abs_to_rel([100, 200, 200, 50], [400, 200])
#     [0.25, 1.0, 0.5, 0.25]
#     """
#     x0, y0, x1, y1 = xyxy
#     w, h = image_wh
#     return type(xyxy)((
#         x0 / w, y0 / h,
#         x1 / w, y1 / h
#     ))
#
#
# def xyxy_rel_to_abs_int(xyxy: np.ndarray, image_wh: np.ndarray) -> np.ndarray:
#     """
#     Converts a bounding box from format (x, y, width, height) or (x, y, x, y) from relative to absolute values
#     with respect to image width and height.
#
#     Parameters
#     ----------
#     xyxy : tuple or list. (x, y, width, height) or (x, y, x, y).
#     image_wh : tuple of width and height of image
#
#     >>> xyxy_rel_to_abs_int([0.25, 1.0, 0.5, 0.25], [400, 200])
#     [100, 200, 200, 50]
#     """
#     x0, y0, x1, y1 = xyxy
#     w, h = image_wh
#     return type(xyxy)((
#         int(x0 * w), int(y0 * h),
#         int(x1 * w), int(y1 * h)
#     ))
#
#
