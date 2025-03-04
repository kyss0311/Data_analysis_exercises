import numpy as np
import random
# 運算上array比list有效率 也比較省空間

L1 = [1, 2, 3]
for i in range(len(L1)):
    L1[i] += 1
print(L1, '\n')

L2 = [1, 2, 3]
A = np.array(L2)
A += 1
print(A, '\n')

b = np.array([[1, 2, 3], [4, 5, 6]])
for i in b:
    for item in i:
        print(item, end=' ')
    print()
print()
# 更改陣列值
b[1, 1] = 8
print(b, '\n')

# 建立指定元素的陣列
c = np.array([1, 2, 3, 4, 5], int)
print(c, '\n')

d = np.array([1, 2, 3, 4, 5], dtype=float)
print(d, '\n')


e = np.arange(5)
print(e, '\n')

f = np.arange(1, 10, 2)
print(f, '\n')

g = np.zeros((2, 3))
print(g, '\n')

h = np.ones((3, 2))
print(h, '\n')

k = np.random.rand(2, 3)
print(k, '\n')
