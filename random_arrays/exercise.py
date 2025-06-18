import numpy as np

rng = np.random.default_rng(12345)

ages = rng.integers(1, 100, 100)

print(ages)