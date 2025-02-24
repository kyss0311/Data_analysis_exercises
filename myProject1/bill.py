win = open('D:\Python 3.10\myproject\myProject1\win').read().split()
mine = open('D:\Python 3.10\myproject\myProject1\mine').read().split()
sum = 0
# enumerate(mine) 逐一的讀取mine裡面的資料
for i, num_mine in enumerate(mine):
    for num_win in win:
        accumulation = 0
        for x in range(6, -1, -1):
            # print(num_mine[x], num_win[x])
            if int(num_mine[x]) != int(num_win[x]):
                break
            else:
                accumulation += 1

        if accumulation == 7:
            sum += 5000
        elif accumulation == 6:
            sum += 2000
        elif accumulation == 5:
            sum += 1000
        elif accumulation == 4:
            sum += 500
        elif accumulation == 3:
            sum += 200
        if accumulation > 2:
            print("中了第", i+1, "張發票,中了", accumulation, "個數字", "累積金額", sum)
            print(num_mine, num_win, "中獎數字：", num_mine[-accumulation:])
            print("-----------------------")



sum = 0
for i, num_mine in enumerate(mine):
    for num_win in win:
        if num_mine[-7:] == num_win[-7:]:
            print("第", i+1, "張發票中獎號碼", num_mine[-7:])
            sum += 5000
        elif num_mine[-6:] == num_win[-6:]:
            print("第", i+1, "張發票中獎號碼", num_mine[-6:])
            sum += 2000
        elif num_mine[-5:] == num_win[-5:]:
            print("第", i+1, "張發票中獎號碼", num_mine[-5:])
            sum += 1000
        elif num_mine[-4:] == num_win[-4:]:
            print("第", i+1, "張發票中獎號碼", num_mine[-4:])
            sum += 500
        elif num_mine[-3:] == num_win[-3:]:
            print("第", i+1, "張發票中獎號碼", num_mine[-3:])
            sum += 200
print("獲得獎金", sum, "元")
