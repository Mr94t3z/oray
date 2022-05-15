import numpy as np
# ex 1
hasil = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
print("Hasil ke-1:", hasil.shape)

# ex 2
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([1, 2, 3, 4, 5])
arr3 = arr1 + arr2
print("Hasil ke-2:", arr3)

# ex 4
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([1, 2, 3, 4, 5])
arr3 = np.power(arr1, 2)
print("Hasil ke-3:", arr3)

# ex 5
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print("Hasil ke-4:", x[1:7:2])

# ex 6
values = np.arange(100, 200, 10)
values = values.reshape(5, 2)
values = values.reshape(1, -1)
print("Hasil ke-5:", values)
