from numpy.random import default_rng

rng = default_rng(12345)

random_arry = rng.random(10)
print("Random array:", random_arry)

mean, stdev = 5, 1
random_normal_arry = rng.normal(mean, stdev, 10)
print("Random normal array:", random_normal_arry)