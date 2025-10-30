#comparing mean and weighted average using numpy
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Unweighted average (same as np.mean)
avg_unweighted = np.average(arr)
print(avg_unweighted) # Output: 3.0

# Weighted average
weights = np.array([0.1, 0.2, 0.3, 0.2, 0.2]) # Example weights
avg_weighted = np.average(arr, weights=weights)
print(avg_weighted) # Output: 3.2 