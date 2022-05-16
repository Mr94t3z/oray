import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

print("\nHasil ke-0:", np.arange(0, 10, 3))

print("\nHasil ke-1:\n", np.zeros((2, 3)))

print("\nHasil ke-2:", np.ones(4))

print("\nHasil ke-3:\n", np.eye(5))

print("\nHasil ke-4:\n", np.linspace(0, 5, 10))

print("\nHasil ke-5:", np.linspace(0, 3, 3))

print("\nHasil ke-6:", np.random.rand(5))

print("\nHasil ke-7:", np.random.randn(4))

# print("\n", sns.displot(np.random.randn(10000), kde=True))

# seaborn 1
print("\nHasil ke-8:")
sns.set_theme()
np.random.seed(0)
x = np.random.randn(10000)
ax = sns.histplot(x)
plt.title('Grafik Randn')
plt.show()

# seaborn 2
print("\nHasil ke-9:")
sns.set_theme()
np.random.seed(0)
x = np.random.rand(10000)
ax = sns.histplot(x)
plt.title('Grafik Rand')
plt.show()

# randint
print("\nHasil ke-10:", np.random.randint(1, 100, 10))

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mat = np.array(matrix)

print("\nHasil ke-11:\n", mat)

print("\nHasil ke-12:", mat.reshape(9,))

print("\nHasil ke-13:", mat.reshape(1, -1))

print("\nHasil ke-14:", mat[2][0])

mat[2][0] = 100

print("\nHasil ke-15:\n", mat)

print("\nHasil ke-16:\n", mat[1:])

print("\nHasil ke-17:\n", mat[1:] > 50)
