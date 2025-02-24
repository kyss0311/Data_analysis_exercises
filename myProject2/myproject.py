import csv

with open("address_data.csv") as fin:
    all_data = list(csv.DictReader(fin))
    for data in all_data:
        print(data["姓名"], data["縣市"], data["住址"])
        if "台" in (data["縣市"] or data["住址"]):
            data["縣市"], data["住址"] = data["縣市"].replace("台", "臺"), data["住址"].replace("台", "臺")
        if "F" in data["住址"]:
            data["住址"] = data["住址"].replace("F", "樓")
        if (data["縣市"] == "臺中市") and ("中港路" in data["住址"]):
            data["住址"] = data["住址"].replace("中港路", "臺灣大道")
        data["住址"] = data["縣市"] + data["住址"]
        print(data["姓名"], data["縣市"], data["住址"])

with open("new_data.csv", "wt", newline='') as fout:
    writer = csv.DictWriter(fout, fieldnames=all_data[0].keys())
    writer.writeheader()
    for data in all_data:
        writer.writerow(data)
