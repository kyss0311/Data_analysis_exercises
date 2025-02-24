import matplotlib.pyplot as plt

data = []
with open("student_score.csv") as fin:
    text = fin.read().split()
    captions = text[0].split(',')
    for e in text[1:]:
        stu = e.split(',')
        scores = [float(sc) for sc in stu[1:]]
        data.append([stu[0]] + scores)

avg = []
for i in range(1, len(data[0])):
    all_scores = [data[stu][i] for stu in range(len(data))]
    avg.append(sum(all_scores)/len(all_scores))

for stu in data:
    name = stu[0]
    scores = stu[1:]
    # 設定新圖表 每位學生才會有自己的圖表
    plt.clf()
    # marker = 'o'圖表會有點點
    plt.plot(scores, marker='o', label='Your score')
    plt.plot(avg, marker='x', label='Class score')
    # 設定標題
    plt.title(name)
    # 設定x軸的資料刻度 文字
    plt.xticks(range(len(scores)), captions[1:])
    # 設定xy軸的標題
    plt.xlabel("Items")
    plt.ylabel("Scores")
    # 設定y軸範圍
    plt.ylim(0, 110)
    # 將圖表內容限縮載圖表範圍
    plt.tight_layout()
    # 儲存圖表
    plt.savefig(name+'.png')
    plt.show()
