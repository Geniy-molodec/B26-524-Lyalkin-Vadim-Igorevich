import csv
with open("products.csv", mode="r", encoding="utf-8") as f:
    reader=csv.DictReader(f)
    expensive=[]
    for product in reader:
        if int(product["price"])>100:
            expensive.append(product)
    with open("expensive.csv", mode="w", encoding="utf-8", newline='') as new_f:
        fieldnames=[]
        for key in list(expensive[0].keys()):
            fieldnames.append(key)
        writer=csv.DictWriter(new_f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expensive)