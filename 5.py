import json
with open("students.json", mode="r", encoding="utf-8") as f:
    max_bal=0
    max_bal_std=''
    reader=json.load(f)
    for student in reader:
        if student["score"]>=60:
            student["passed"]=True
        else:
            student["passed"]=False
        if student["score"]>max_bal:
            max_bal=student["score"]
    with open("students_new.json", mode="w", encoding="utf-8") as new_f:
        json.dump(reader,new_f)