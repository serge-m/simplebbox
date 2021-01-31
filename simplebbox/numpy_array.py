import numpy as np
from simplebbox._array_processor import ArrayProcessor


def _np_stack_last_axis(arrays):
    return np.stack(arrays, axis=-1)


bbox_numpy = ArrayProcessor(stack_fn=_np_stack_last_axis)
