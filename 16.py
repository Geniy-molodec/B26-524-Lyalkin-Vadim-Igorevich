import re
with open("logs16.txt", mode="r", encoding="utf-8") as f:
    info_count=0
    warning_count=0
    error_count=0
    user_ids_error=[]
    line_info = re.compile(r".*INFO.*")
    line_error = re.compile(r".*ERROR.*")
    line_warning = re.compile(r".*WARNING.*")
    for line in f:
        line=line.strip()
        if line_info.match(line):
            info_count+=1
        elif line_error.match(line):
            error_count+=1
            user_ids_error.append(re.findall(r".*ERROR User (\d+).*", line)[0])
        elif line_warning.match(line):
            warning_count+=1

    print(f"INFO: {info_count}")
    print(f"WARNING: {warning_count}")
    print(f"ERROR: {error_count}")
    print(f"Пользователи для которых встречались ошибки: {list(set(user_ids_error))}")

