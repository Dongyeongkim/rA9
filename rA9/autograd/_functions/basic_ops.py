import jax.numpy as np

from ..function import Function


class Add(Function):
    id = "Add"

    @staticmethod
    def forward(ctx, a, b):
        def np_fn(a, b):
            return np.add(a,b)

        id = "Add"
        np_args = (a.data, b.data)
        return np_fn, np_args, np_fn(*np_args),id

    @staticmethod
    def backward(ctx, grad_output):
        return super(Add, Add).backward(ctx, grad_output)


def sort_args(a, b):
    return (a, b, True) if isinstance(a, np.ndarray) else (b, a, False)


class View(Function):
    id = "View"

    @staticmethod
    def forward(ctx, a, sizes):
        def np_fn(a, sizes):
            return np.reshape(a, sizes)

        id = "View"
        np_args = (a.data, sizes)
        return np_fn, np_args, np_fn(*np_args),id

    @staticmethod
    def backward(ctx, grad_output):
        return super(View, View).backward(ctx, grad_output)
