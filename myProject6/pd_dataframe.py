import pandas as pd
import numpy as np
import matplotlib

# data = {
#     "名稱": ["客戶A","客戶B","客戶A","客戶B","客戶A","客戶B","客戶A","客戶A",],
#     "編號": ["訂單1","訂單1","訂單2","訂單3","訂單2","訂單2","訂單1","訂單3"],
#     "數量": [4,4,1,2,3,4,2,1],
#     "售價": [495,496,360,451,221,321,466,260]
# }
# df = pd.DataFrame(data)
# print(df)
# df.groupby('名稱').sum()
# print(df.groupby('名稱').sum())

# products = {
#     'channel': ["網路", "網路", "電视", "電视", "郵購", "郵購"],
#     "company": ["EHS", "Momo", "EHS", "Viva", "Momo", "EHS"],
#     "sales": [11.22, 23.50, 12.99, 15.95, 25.75, 11.55]
# }
#
# oridnals = ["A", "B", "C", "D", "E", "F"]
# df = pd.DataFrame(products, index=oridnals)
# print(df, '\n')
# score = [4, 3, 5, 2, 8, 6]
# df["score"] = score
# # print(df)
#
# # 樞紐分析表
# pivot_tb = df.pivot_table(index='channel', columns='company', values='sales')
# print(pivot_tb)
#
# # 統計學 describe()
# print(df['sales'].describe())
# print(df.describe())

df3 = pd.DataFrame(np.random.randn(100, 4), index=pd.date_range('05/20/2021', periods=100), columns=list('ABCD'))
df3 = df3.cumsum()
df3.plot()
df3.plot(kind='bar')