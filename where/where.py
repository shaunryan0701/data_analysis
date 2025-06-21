import numpy as np

ages = np.array([5, 10, 25, 34, 49, 60])

adult_ages = np.where(ages >= 18)
print("Indices of adult ages:", adult_ages)
print("Adult ages:", ages[adult_ages])