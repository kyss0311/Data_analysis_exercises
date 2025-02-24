import csv
from collections import Counter

# 讀取資料 塞選資料
with open("中華職棒球員打擊數據.csv") as fin:
    datas = list(csv.DictReader(fin))
    name = []
    for data in datas:
        if int(data["全壘打"]) >= 10 and int(data["盜壘"]) >= 10:
            name.append(data)
            print(data["姓名"], data["全壘打"], data["盜壘"])

# 統計資料
counts = Counter(data["姓名"] for data in name)
print("共有", len(counts), "人有此成就")
# 找出做多次的三人
for r, p in enumerate(counts.most_common(3)):
    n, times = p[0], p[1]
    print('第', r+1, '名：', n, '紀錄達成', times, '次')
    for e in name:
        if e['姓名'] == n:
            print(n, e["年度"], e["全壘打"], e["盜壘"])


#

# with open("中華職棒球員打擊數據.csv") as fin:
#     datas = list(csv.DictReader(fin))
#     name = {}
#     for data in datas:
#         if int(data["全壘打"]) >= 10 and int(data["盜壘"]) >= 10:
#
#             if name.get(data["姓名"]):
#                 name[data["姓名"]] += 1
#             else:
#                 name[data["姓名"]] = 1
#             print(name[str(data["姓名"])])
#             print(data["姓名"], data["全壘打"], data["盜壘"])
#     print(name)
#     print("共有", len(name), "人有此成就")
#     sorted(name.values())
