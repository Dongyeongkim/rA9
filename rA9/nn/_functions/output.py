from jax import jit
import jax.numpy as jnp
from rA9.autograd import Function
from rA9.autograd import Variable


class Output(Function):
    id = 'output'

    @staticmethod
    def forward(ctx, input, weights, v_current, tau_m, dt, time_step):
        assert isinstance(input, Variable)
        assert isinstance(v_current, Variable)
        assert isinstance(weights, Variable)

        def np_fn(input_np, weights_np, v_current, time_step, dt, tau_m):
            return jnp.divide(
                jnp.divide(
                    (
                        jnp.multiply
                            (
                            jnp.subtract
                                (
                                jnp.matmul
                                    (
                                    input_np,
                                    weights_np
                                ),
                                v_current.data
                            ),
                            dt
                        )
                    )
                    , tau_m
                )
                , time_step)

        np_args = (input.data, weights.data,v_current, time_step, dt, tau_m)

        return np_fn, np_args, np_fn(*np_args)

    @staticmethod
    def backward(ctx, grad_outputs):
        super(Output, Output).backward(ctx, grad_outputs)