import csv
with open("students.csv", mode='r', encoding="utf-8") as f:
    sum_bal=0
    kol_std=0
    max_bal=0
    max_bal_std=""
    sum_bal_group={}
    kol_std_group={}
    reader=csv.DictReader(f)
    for student in reader:
        name=student["name"]
        group=student["group"]
        bal=student["score"]
        sum_bal+=int(bal)
        kol_std+=1
        if int(bal)>max_bal:
            max_bal=int(bal)
            max_bal_std=name
        try:
            sum_bal_group[group]+=int(bal)
        except KeyError:
            sum_bal_group[group]=int(bal)
        try:
            kol_std_group[group]+=1
        except KeyError:
            kol_std_group[group]=1
    print(f'Средний балл всех студентов: {sum_bal/kol_std}')
    print(f'Студент с максимальным баллом: {max_bal_std}')
    for key in sum_bal_group.keys():
        print(f'Средний балл группы {key}: {sum_bal_group[key]/kol_std_group[key]}')
