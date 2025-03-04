import numpy as np

# 當作向量看
a = np.array([1, 2, 3])
print('a=', a)
print('a+1=', a+1)
print('a*2=', a*2, '\n')
s = np.array([2, 3, 4])
print('a+s=', a+s)
print('a*s=', a*s)
print('a。s=', a.dot(s))  # 點積運算

# a到s的距離
a_s = a - s
a_s = np.linalg.norm(a_s)
print('a到s的距離=', a_s)


# array的切割 array[start:end:step] 不包含end  ex:c[0:6] = [1 2 3 4 5 6] 不是 [1 2 3 4 5 6 7]
c = np.array([1, 2, 3, 4, 5, 6, 7])
print(c[0:6], c[:5], c[1:6:2])
print(c[::2], c[2::], c[-1:])
print(c[::-1])


# 矩陣 二維運算
a = np.array([[1, 2], [4, 5]])
b = np.array([[1, 3], [2, 4]])

print('a+b=\n',a+b)
c = a.dot(b)
print(c)  # 1*1+2*2, 1*3+2*4
          # 4*1+5*2, 4*3+5*4

d = np.arange(1, 26)
print(d)
# 將依微陣列轉換成二微陣列 m*n  列row*行column
d = d.reshape(5, 5)
print(d, '\n')

# 矩陣切割
print(d[0, 1:4], d[2, 2:5])
print(d[1:4, 1], d[2:5, 3])
print(d[1:4, 1:4])
print(d[1:4:2, 1:4:2])
print()
print(d[::2, ::2])
print(d[::-1, ::-1],'\n\n')


# 進階索引值
e = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
f = e[[0, 2, 9]]
print(f)

mask = (e % 3 == 0)
print(mask)

g = np.arange(1, 37)
g = g.reshape(6, 6)
print(g)
print(g[(0, 1, 2, 3, 4),(1, 2, 3, 4, 5)])
print(g[3:, [0, 2, 5]])
# 重要!!!!!
mask = np.array([1, 0, 1, 0, 0, 1], dtype=np.bool)
print(g[mask, 2])

# 平坦化 & 轉置transpose   [2x3]*[2x3] 時不能直接乘法 要線轉置 [2x3]*[2x3].T = [2x3]*[3x2]  (mxn  nxk 才可以乘法)
h = np.array([[1, 2, 3], [4, 5, 6]])
print(h, '\n')
print(h.ravel(), '\n')
# print(np.ravel(h))
print(h.T, '\n')
# print(h.transpose())

# 新增陣列維度
k = np.array([1, 2, 3])
print(k, '\n')
p = k[:, np.newaxis]
print(p, '\n')

k = np.array([[1, 2, 3], [4, 5, 6],[7, 8, 9]])
print(k, '\n')
p = k[:, np.newaxis]
print(p, '\n')

# 複製 連結
q = np.array([1, 2])
print(q, '\n')
r = q.copy()
print(r, '\n')
r.fill(6)  # r改動時不會影響q  如果用 r=q  r改動時q也會跟者改動
print(r, '\n')
print(np.concatenate((q, r)), '\n')

s = np.array([[1, 2], [3, 4]])
t = np.array([[5, 6], [7, 8]])
print(np.concatenate((s, t)), '\n')  # axis預設值為0
print(np.concatenate((s, t), axis=1), '\n')

# 陣列廣播
u = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 1, 1]])
v = np.array([1, 0, 1])
print(u+v)


# 隨機取變數
w = np.arange(0, 100, 10, dtype=np.floating)
print(w)

index = np.random.randint(0, len(w), 5)
print(index)
print(w[index])

# 取整數位
x = np.array([0.256, 6.452, 8.166, -3.025, 233.023])
print(x)
print(np.floor(x))  # 往下取整數
print(np.ceil(x))  # 往上取整數

# 計算
y = np.array([[1, 2, 3], [4, 5, 6]])
print(np.sum(y))
print('縱向求和=', np.sum(y, axis=0))
print('橫向求和=', np.sum(y, axis=1))
print('平均數', np.mean(y))
print('縱向平均數', np.mean(y, axis=0))
print('橫向平均數', np.mean(y, axis=1))

weight = [0.3, 0.7]  # 設定權重
print(np.average(y, axis=0, weights=weight))  # 0.3*1+0.7*4  0.3*2+0.7*5  0.3*3+0.7*6

print('最大值', np.max(y))
print('全部標準差', np.std(y))
print('每一行的標準差', np.std(y, axis=0))
print('每一列的標準差', np.std(y, axis=1))


# 基礎
z1 = np.array([0, 5, 6, 4, 3, 8, 9, 1, 0, 10, -6])
z2 = np.array([0, 5, 8, 4, 3, 8, 1, 1, 0, 10, -6])
print(np.argmax(z1))  # 最大值的索引
print(np.where(z1 != z2))  # z1!=z2的地方
print(np.where(z1 < 5, 0, 1))  # z1中小於五的值為0 大於五為1
# z1中小於2的值乘2 大於7乘3 其餘元素變成0
print(np.piecewise(z1, [z1 < 2, z1 > 7], [lambda x:x*2, lambda x:x*3]))
