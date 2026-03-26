"""
Day 44 Activity: Log, Exp, Softmax

Tasks:

1) Implement stable softmax

2) Apply to score vector

3) Show sum of probabilities

"""
import numpy as np

# TODO: Implement softmax_stable

xs = np.array([-3, -1, 0, 1, 3])
exp_xs = np.exp(xs)
print("x:", xs, "\nexp(x):", exp_xs)

# TODO: Apply to scores

xs_stable = xs - np.max(xs)
exp_xs_stable = np.exp(xs_stable)
print("x (stable):", xs_stable, "\nexp(x) (stable):", exp_xs_stable)
print("Sum of probabilities:", np.sum(exp_xs_stable))