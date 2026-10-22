with open("text.txt", mode="r", encoding="utf-8") as f:
    lines=0
    words=0
    chars=0
    max_len=-1
    for line in f:
        line=line.rstrip("\n")
        lines+=1
        words+=len(line.split())
        line_len=len(line)
        chars+=line_len
        if max_len<line_len:
            max_len=line_len
    print(f'Количество строк: {lines}')
    print(f'Количество слов: {words}')
    print(f'Количесвто символов: {chars}')
    print(f'Длина самой длинной строки: {max_len}')
