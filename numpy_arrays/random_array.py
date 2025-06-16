from numpy.random import default_rng

rng = default_rng(12345)

random_arry = rng.random(10)
print("Random array:", random_arry)