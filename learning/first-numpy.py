import numpy as np

my_list = [1, 2, 3, 4, 5]
print("\nHasil ke-0:", type(my_list))

arr = np.array(my_list)
print("\nHasil ke-1:", type(arr))

print("\nHasil ke-2:", arr.dtype)

arr2 = np.array(my_list, dtype='int64')

print("\nHasil ke-3:", arr2.ndim)

# tambah
print("\nHasil ke-4:", arr + arr2)

# pangkat
print("\nHasil ke-5:", arr**2)

# akar
print("\nHasil ke-6:", np.sqrt(arr))

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

mat = np.array(matrix)

print("\nHasil ke-7:", mat.ndim)

print("\nHasil ke-8:", mat.shape)

print("\nHasil ke-9:\n", mat)
