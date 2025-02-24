results = []
# 讀取資料
with open("student.csv") as fin:
    data = fin.read().split()
    # 從第二筆資料開始取 第一筆是名稱
    for scores in data[1:]:
        stu = scores.split(',')
        # score 存放成績 第一筆資料是姓名
        score = [int(sc) for sc in stu[1:]]
        # 把作業由小排到大 取後兩個做平均
        hw_average = sum(sorted(score[0:3])[1:])/2
        exam_average = score[3]*0.2+score[4]*0.3
        final = round(hw_average*0.5+exam_average, 2)
        print(stu[0], score, " 作業平均=", hw_average, "總平均=", final)
        stu.append(str(final))
        results.append(stu)

with open("finally.csv", "w") as fout:
    fout.write(data[0]+",總成績\n")
    for stu in results:
        fout.write(','.join([str(e) for e in stu]) + '\n')
