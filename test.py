import csv
with open("products.csv", mode="r", encoding="utf-8") as f:
    reader=csv.DictReader(f)

    print(fieldnames)