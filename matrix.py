import numpy as np
a = np.array([[7.09, 1.17, 2.23], [0.61, 0.71, -0.05], [-1.03, -2.05, 0.877]])
for i in range(len(a)):
	if a[i][i] == 0:
		for j in range(i + 1, len(a)):
			if a[j][i] != 0:
				a[[i, j]] = a[[j, i]]
	break
for j in range(i + 1, len(a)):
	factor = a[j][i] / a[i][i]
	a[j] -= factor * a[i]
dt = 1
for i in range(len(a)):
	dt *= a[i][i]
print("Определитель матрицы равен:", round(dt,6))