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

        The function can process batch inputs. In this case representation of each bounding box
        must be stored as the last axis of the array.

        """
        arr = x0y0wh
        res = [
            arr[..., 0],
            arr[..., 1],
            arr[..., 0] + arr[..., 2],
            arr[..., 1] + arr[..., 3]
        ]
        return self.stack(res).reshape(*arr.shape[:-1], len(res))

    def x0y0x1y1_to_x0y0wh(self, x0y0x1y1):
        """
        Converts a bounding box from format
        (min x, min y, max x, max y) to
        (min x, min y, width, height).

        In the coordinate system of a screen (min x, min y) corresponds to the left top corner of the box.

        The function can process batch inputs. In this case representation of each bounding box
        must be stored as the last axis of the array.
        """
        arr = x0y0x1y1
        res = [
            arr[..., 0],
            arr[..., 1],
            arr[..., 2] - arr[..., 0],
            arr[..., 3] - arr[..., 1]
        ]
        return self.stack(res).reshape(*arr.shape[:-1], len(res))

    def cxcywh_to_x0y0wh(self, cxcywh):
        """
        Converts a bounding box from format
        (center x, center y, width, height) to
        (min x, min y, width, height).

        In the coordinate system of a screen (min x, min y) corresponds to the left top corner of the box.

        The function can process batch inputs. In this case representation of each bounding box
        must be stored as the last axis of the array.

        """
        arr = cxcywh
        res = [
            arr[..., 0] - arr[..., 2] / 2,
            arr[..., 1] - arr[..., 3] / 2,
            arr[..., 2],
            arr[..., 3]
        ]
        return self.stack(res).reshape(*arr.shape[:-1], len(res))

    def cxcywh_to_x0y0wh_int_div(self, cxcywh):
        """
        Converts a bounding box from format
        (center x, center y, width, height) to
        (min x, min y, width, height)
        using integer operations (division).

        In the coordinate system of a screen (min x, min y) corresponds to the left top corner of the box.
        """
        arr = cxcywh
        res = [
            arr[..., 0] - arr[..., 2] // 2,
            arr[..., 1] - arr[..., 3] // 2,
            arr[..., 2],
            arr[..., 3]
        ]
        return self.stack(res).reshape(*arr.shape[:-1], len(res))

    def cxcywh_to_x0y0x1y1(self, cxcywh):
        """
        Converts a bounding box from format
        (center x, center y, width, height) to
        (min x, min y, max x, max y).

        In the coordinate system of a screen (min x, min y) corresponds to the left top corner of the box.
        """
        arr = cxcywh
        x0 = arr[..., 0] - arr[..., 2] / 2
        y0 = arr[..., 1] - arr[..., 3] / 2
        res = [
            x0,
            y0,
            x0 + arr[..., 2],
            y0 + arr[..., 3]
        ]
        return self.stack(res).reshape(*arr.shape[:-1], len(res))

    def cxcywh_to_x0y0x1y1_int_div(self, cxcywh):
        """
        Converts a bounding box from format
        (center x, center y, width, height) to
        (min x, min y, max x, max y) using only integer division.

        In the coordinate system of a screen (min x, min y) corresponds to the left top corner of the box.
        """
        arr = cxcywh
        x0 = arr[..., 0] - arr[..., 2] // 2
        y0 = arr[..., 1] - arr[..., 3] // 2
        res = [
            x0,
            y0,
            x0 + arr[..., 2],
            y0 + arr[..., 3]
        ]
        return self.stack(res).reshape(*arr.shape[:-1], len(res))


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
