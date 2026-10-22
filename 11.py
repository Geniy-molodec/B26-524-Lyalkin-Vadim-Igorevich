import re
with open("logs.txt", encoding="utf-8") as f:
    log=f.read()
    user_ids=re.findall(r"User (\d+)", log)
    print(f"Идентификаторы пользователей: {list(set(user_ids))}")
    error_log=re.findall(r"^ERROR.*$", log, re.M)
    print(f"Все строки с ERROR: {error_log}")
    user_ids_errors=re.findall(r"ERROR User (\d+)", log)
    print(f"Идентификаторы пользователей, для которых произошла ошибка: {list(set(user_ids_errors))}")

