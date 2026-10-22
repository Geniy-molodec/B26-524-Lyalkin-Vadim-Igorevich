with open("numbers.txt", "r", encoding="utf-8") as f:
    mmin = 10**9
    mmax = -10**9
    ssum = 0
    llen = 0

    for line in f:
        stroka = line.strip()
        if not stroka:
            continue

        if stroka.lstrip('-').isdigit():
            num = int(stroka)
            llen += 1
            ssum += num
            if num > mmax:
                mmax = num
            if num < mmin:
                mmin = num

    if llen > 0:
        sred = ssum / llen
        with open("result.txt", "w", encoding="utf-8") as g:
            g.write(f"максимальное число: {mmax}\n")
            g.write(f"минимальное число: {mmin}\n")
            g.write(f"среднее арифметическое: {sred}")
    else:
        print("В файле не найдено ни одного числа")