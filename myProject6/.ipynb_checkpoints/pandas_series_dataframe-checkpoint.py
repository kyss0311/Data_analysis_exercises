import pandas as pd
from numpy.random import randint
# Series用法
s = pd.Series([12, 29, 72, 4])
print(s)

fruits = ['蘋果', '橘子', '梨子']
quantities = [15, 33, 45]
s = pd.Series(quantities, index=fruits)
print(s)
print(s.index)
print(s.values)
print(s['橘子'])
print(s[['橘子', '梨子']])
print((s+2)*3)

# DataFrame用法
fruits = {
    'apple': [4, 3, 1, 3],
    'banana': [0, 4, 6, 2],
    'orange': [1, 5, 2, 4]
}
cites = ['台北', '新北', '台中', '高雄']
df = pd.DataFrame(fruits, index=cites)
print(df)

# columns定義欄位順序
df = pd.DataFrame(fruits, columns=['banana', 'orange', 'apple'], index=cites)
# print(df)
# 更改df 用df.
cites[1] = '桃園'
df.index = cites
print(df)

# 轉置
print(df.T)

# 匯出dataframe
df.to_csv("df_csv.csv")
df.to_json("df_json.json")
df.to_html("df_html.html")

# 只讀取 前幾筆資料 或後幾筆資料
print(df.head(3))
print(df.tail(2))

# 顯示幾筆資料  形狀  資訊
print(len(df))
print(df.shape)
print(df.info())

# 走訪資料
for index, row in df.iterrows():
    print(index, row["banana"])

# 選取資料
products = {
    'channel': ["網路", "網路", "電视", "電视", "郵購", "郵購"],
    "company": ["EHS", "Momo", "EHS", "Viva", "Momo", "EHS"],
    "sales": [11.22, 23.50, 12.99, 15.95, 25.75, 11.55]
}

oridnals = ["A", "B", "C", "D", "E", "F"]
df = pd.DataFrame(products, index=oridnals)
# print(df)
# print(df[['company', 'sales']].head(3))
# print(df[0:2])
# print(df[3:])
# print(df['C':'E'])  # 會包含最後一筆E
# print(df[df.sales > 15])
# print(df[(df.sales > 15) & (df.sales < 25)])

# # 排序資料 ascending=False 大到小 True 小到大
# print(df.sort_values("sales", ascending=False))

# # 將資料變成索引值
# df.set_index("sales", inplace=True)  # inplace 會直接修改資料
# print(df.sort_index(axis=0, ascending=False))  # axis = 0 變成第一欄  ascending=False大到小

# # 更新資料
# print(df)
# df.loc['A', 'sales'] = 9.6
# df.iloc[1, 2] = 22.01
# print(df)
#
# r = ['郵購', 'viva', 18.9]
# df.loc['C'] = r
# print(df)
#
# s = [10, 20, 30, 40, 50, 60]
# df.loc[ : , 'sales'] = s
# print(df)

# # 刪除資料
# df.loc['A', 'sales'] = None
# df.iloc[1, 2] = None
# print(df)
#
df2 = df.drop(['B', 'D'])
# print(df2)
# df2 = df2.drop(['sales'], axis=1)
# print(df2)

# 新增資料
df2.loc['H'] = ['網路', 'vavi', 16.5]
print(df2)

df.loc[:, 'items'] = randint(100, 120, size=len(df))
print(df)
