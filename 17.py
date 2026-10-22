with open("numbers17.txt", mode="r", encoding="utf-8") as f:
    total=0
    count=0
    minimum=None
    maximum=None
    for line in f:
        line=line.strip()
        num=int(line)
        count+=1
        total+=num
        if minimum is None or minimum>num:
            minimum=num
        if maximum is None or maximum<num:
            maximum=num
    print(f"Сумма: {total}")
    print(f"Минимум: {minimum}")
    print(f"Максимум: {maximum}")
    print(f"Количество: {count}")
    print(f"Среднее: {total/count}")