# How to flatten only some Dimensions of a NumPy array

import numpy as np

arr = np.zeros((2, 4, 2))
print(arr)

print('-' * 50)

new_arr = arr.reshape(8, 2)
print(new_arr)