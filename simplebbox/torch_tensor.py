import torch
from simplebbox._array_processor import ArrayProcessor


def _torch_stack_last_axis(arrays):
    return torch.stack(arrays, axis=-1)


bbox_torch = ArrayProcessor(stack_fn=_torch_stack_last_axis)
